#!/usr/bin/env python3
"""
Leaves.yml 配置文件 GUI 编辑器
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yaml
import os
from collections import OrderedDict
import re

class LeavesConfigEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Leaves.yml 配置编辑器")
        self.root.geometry("800x600")
        
        # 配置文件路径
        self.config_file = "../leaves.yml"
        
        # 存储控件引用
        self.widgets = {}
        
        # 存储变量引用
        self.vars = {}
        
        # 存储滚动框架引用
        self.scrollable_frames = {}
        
        # 创建界面
        self.create_widgets()
        
        # 加载配置
        self.load_config()
    
    def create_widgets(self):
        # 创建主框架
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # 创建顶部框架（文件操作）
        top_frame = ttk.Frame(main_frame)
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(master=top_frame, text="加载配置", command=self.load_config).pack(side=tk.LEFT)
        ttk.Button(master=top_frame, text="保存配置", command=self.save_config).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Button(master=top_frame, text="另存为", command=self.save_as_config).pack(side=tk.LEFT, padx=(5, 0))
        
        # 创建notebook用于分类显示配置
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # 创建各个配置分类的标签页
        self.settings_frame = ttk.Frame(self.notebook)
        self.modify_frame = ttk.Frame(self.notebook)
        self.performance_frame = ttk.Frame(self.notebook)
        self.protocol_frame = ttk.Frame(self.notebook)
        self.region_frame = ttk.Frame(self.notebook)
        self.fix_frame = ttk.Frame(self.notebook)
        
        self.notebook.add(self.settings_frame, text="基础设置")
        self.notebook.add(self.modify_frame, text="游戏机制")
        self.notebook.add(self.performance_frame, text="性能优化")
        self.notebook.add(self.protocol_frame, text="协议支持")
        self.notebook.add(self.region_frame, text="区域文件")
        self.notebook.add(self.fix_frame, text="修复选项")
        
        # 为每个标签页创建滚动区域
        self.create_scrollable_frame(self.settings_frame)
        self.create_scrollable_frame(self.modify_frame)
        self.create_scrollable_frame(self.performance_frame)
        self.create_scrollable_frame(self.protocol_frame)
        self.create_scrollable_frame(self.region_frame)
        self.create_scrollable_frame(self.fix_frame)
        
        # 创建状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(10, 0))
    
    def create_scrollable_frame(self, parent):
        """创建带滚动条的框架"""
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # 将滚动区域存储在父框架的属性中
        parent.scrollable_frame = scrollable_frame
        self.scrollable_frames[parent] = scrollable_frame
        
        # 绑定鼠标滚轮事件
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        canvas.bind_all("<MouseWheel>", _on_mousewheel)
    
    def load_config(self):
        """加载配置文件"""
        try:
            if not os.path.exists(self.config_file):
                messagebox.showerror("错误", f"配置文件 {self.config_file} 不存在")
                return
            
            with open(self.config_file, 'r', encoding='utf-8') as f:
                # 读取原始内容以保留注释
                content = f.read()
            
            # 解析YAML
            config = yaml.safe_load(content)
            if config is None:
                config = {}
            
            # 保存原始内容用于注释提取
            self.raw_content = content
            self.config_data = config
            
            # 清除现有控件
            self.clear_widgets()
            
            # 创建配置控件
            self.create_config_widgets()
            
            self.status_var.set(f"已加载配置文件: {self.config_file}")
        except Exception as e:
            messagebox.showerror("错误", f"加载配置文件时出错: {str(e)}")
    
    def clear_widgets(self):
        """清除所有控件"""
        for widget_list in self.widgets.values():
            for widget in widget_list:
                widget.destroy()
        self.widgets.clear()
    
    def create_config_widgets(self):
        """根据配置创建控件"""
        if not hasattr(self, 'config_data'):
            return
        
        # 基础设置
        if 'settings' in self.config_data:
            row = 0
            row = self.create_section_widgets(
                self.scrollable_frames[self.settings_frame], 
                self.config_data['settings'], 
                "", 
                row
            )
        
        # 游戏机制修改
        if 'modify' in self.config_data.get('settings', {}):
            row = 0
            row = self.create_section_widgets(
                self.scrollable_frames[self.modify_frame], 
                self.config_data['settings']['modify'], 
                "settings.modify.", 
                row
            )
        
        # 性能优化
        if 'performance' in self.config_data.get('settings', {}):
            row = 0
            row = self.create_section_widgets(
                self.scrollable_frames[self.performance_frame], 
                self.config_data['settings']['performance'], 
                "settings.performance.", 
                row
            )
        
        # 协议支持
        if 'protocol' in self.config_data.get('settings', {}):
            row = 0
            row = self.create_section_widgets(
                self.scrollable_frames[self.protocol_frame], 
                self.config_data['settings']['protocol'], 
                "settings.protocol.", 
                row
            )
        
        # 区域文件
        if 'region' in self.config_data.get('settings', {}):
            row = 0
            row = self.create_section_widgets(
                self.scrollable_frames[self.region_frame], 
                self.config_data['settings']['region'], 
                "settings.region.", 
                row
            )
        
        # 修复选项
        if 'fix' in self.config_data.get('settings', {}):
            row = 0
            row = self.create_section_widgets(
                self.scrollable_frames[self.fix_frame], 
                self.config_data['settings']['fix'], 
                "settings.fix.", 
                row
            )
    
    def create_section_widgets(self, parent, section_data, prefix, row):
        """创建一个配置部分的控件"""
        for key, value in section_data.items():
            full_key = f"{prefix}{key}"
            
            # 获取注释（简化处理）
            comment = self.extract_comment(full_key)
            
            # 创建标签
            label = ttk.Label(parent, text=key)
            label.grid(row=row, column=0, sticky=tk.W, padx=(10, 5), pady=2)
            
            # 创建控件
            widget = None
            var = None
            if isinstance(value, bool):
                # 布尔值使用复选框
                var = tk.BooleanVar(value=value)
                widget = ttk.Checkbutton(parent, variable=var)
            elif isinstance(value, (int, float)):
                # 数字使用输入框
                var = tk.StringVar(value=str(value))
                widget = ttk.Entry(parent, textvariable=var, width=20)
            elif isinstance(value, str):
                # 字符串使用输入框
                var = tk.StringVar(value=value)
                widget = ttk.Entry(parent, textvariable=var, width=30)
            elif isinstance(value, list):
                # 列表使用文本框
                var = tk.StringVar(value=', '.join(map(str, value)))
                widget = ttk.Entry(parent, textvariable=var, width=40)
            else:
                # 其他类型使用只读标签
                widget = ttk.Label(parent, text=str(value))
            
            if widget:
                widget.grid(row=row, column=1, sticky=tk.W, padx=5, pady=2)
                
                # 添加提示信息
                if comment:
                    tooltip = ttk.Label(parent, text=comment, foreground="gray", font=("Arial", 8))
                    tooltip.grid(row=row, column=2, sticky=tk.W, padx=(5, 0), pady=2)
                
                # 存储控件引用和变量引用
                if full_key not in self.widgets:
                    self.widgets[full_key] = []
                self.widgets[full_key].append(widget)
                
                # 存储变量引用
                if var:
                    self.vars[full_key] = var
            
            row += 1
            
            # 递归处理嵌套结构
            if isinstance(value, dict):
                row = self.create_section_widgets(parent, value, f"{full_key}.", row)
        
        return row
    
    def extract_comment(self, key):
        """从原始内容中提取注释（简化实现）"""
        # 这是一个简化的注释提取方法
        # 实际应用中可能需要更复杂的解析
        lines = self.raw_content.split('\n')
        for i, line in enumerate(lines):
            # 查找包含键的行
            if f"{key.split('.')[-1]}:" in line and '#' in line:
                # 提取注释部分
                comment_match = re.search(r'#\s*(.*)', line)
                if comment_match:
                    return comment_match.group(1)
        return ""
    
    def save_config(self):
        """保存配置到文件"""
        try:
            # 更新配置数据
            self.update_config_data()
            
            # 保存到文件
            with open(self.config_file, 'w', encoding='utf-8') as f:
                yaml.dump(self.config_data, f, allow_unicode=True, indent=2, sort_keys=False)
            
            self.status_var.set(f"配置已保存到: {self.config_file}")
            messagebox.showinfo("成功", "配置已成功保存")
        except Exception as e:
            messagebox.showerror("错误", f"保存配置时出错: {str(e)}")
    
    def save_as_config(self):
        """另存为配置文件"""
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".yml",
                filetypes=[("YAML files", "*.yml"), ("All files", "*.*")]
            )
            
            if file_path:
                # 更新配置数据
                self.update_config_data()
                
                # 保存到文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    yaml.dump(self.config_data, f, allow_unicode=True, indent=2, sort_keys=False)
                
                self.status_var.set(f"配置已保存到: {file_path}")
                messagebox.showinfo("成功", f"配置已成功保存到: {file_path}")
        except Exception as e:
            messagebox.showerror("错误", f"保存配置时出错: {str(e)}")
    
    def update_config_data(self):
        """根据GUI控件更新配置数据"""
        def update_nested_dict(d, keys, value):
            """递归更新嵌套字典"""
            if len(keys) == 1:
                d[keys[0]] = value
            else:
                if keys[0] not in d:
                    d[keys[0]] = {}
                update_nested_dict(d[keys[0]], keys[1:], value)
        
        # 遍历所有控件并更新值
        for full_key, widgets in self.widgets.items():
            if full_key in self.vars:
                var = self.vars[full_key]
                keys = full_key.split('.')
                
                # 获取值并转换类型
                value = var.get()
                
                # 类型转换
                if value.lower() in ['true', 'false']:
                    value = value.lower() == 'true'
                elif value.replace('.', '').replace('-', '').isdigit():
                    if '.' in value:
                        value = float(value)
                    else:
                        value = int(value)
                elif ',' in value:
                    # 处理列表
                    value = [item.strip() for item in value.split(',')]
                
                # 更新配置数据
                current_dict = self.config_data
                update_nested_dict(current_dict, keys, value)

def main():
    root = tk.Tk()
    app = LeavesConfigEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()