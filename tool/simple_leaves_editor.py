#!/usr/bin/env python3
"""
Leaves.yml 简化配置编辑器
专注于最重要的配置项
"""

import tkinter as tk
from tkinter import ttk, messagebox
import yaml
import os

class SimpleLeavesEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Leaves.yml 简化配置编辑器")
        self.root.geometry("600x500")
        
        # 配置文件路径
        self.config_file = "../leaves.yml"
        
        # 配置数据
        self.config_data = {}
        
        # 创建界面
        self.create_widgets()
        
        # 加载配置
        self.load_config()
    
    def create_widgets(self):
        # 创建主框架
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nesw")
        
        # 配置标题
        title_label = ttk.Label(main_frame, text="Leaves 服务器配置", font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # 创建配置区域
        config_frame = ttk.LabelFrame(main_frame, text="重要配置项", padding="10")
        config_frame.grid(row=1, column=0, columnspan=2, sticky="nesw", pady=(0, 20))
        
        # 自动更新设置
        ttk.Label(config_frame, text="自动更新:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.auto_update_var = tk.BooleanVar()
        auto_update_check = ttk.Checkbutton(config_frame, variable=self.auto_update_var)
        auto_update_check.grid(row=0, column=1, sticky=tk.W, pady=5)
        ttk.Label(config_frame, text="启用自动更新功能", foreground="gray").grid(row=0, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # 假人设置
        ttk.Label(config_frame, text="启用假人:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.fakeplayer_var = tk.BooleanVar()
        fakeplayer_check = ttk.Checkbutton(config_frame, variable=self.fakeplayer_var)
        fakeplayer_check.grid(row=1, column=1, sticky=tk.W, pady=5)
        ttk.Label(config_frame, text="启用假人功能", foreground="gray").grid(row=1, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # 假人数量限制
        ttk.Label(config_frame, text="假人数量限制:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.fakeplayer_limit_var = tk.StringVar()
        fakeplayer_limit_entry = ttk.Entry(config_frame, textvariable=self.fakeplayer_limit_var, width=10)
        fakeplayer_limit_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        ttk.Label(config_frame, text="最大假人数量", foreground="gray").grid(row=2, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # 红石剪刀扳手
        ttk.Label(config_frame, text="红石剪刀扳手:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.redstone_shears_var = tk.BooleanVar()
        redstone_shears_check = ttk.Checkbutton(config_frame, variable=self.redstone_shears_var)
        redstone_shears_check.grid(row=3, column=1, sticky=tk.W, pady=5)
        ttk.Label(config_frame, text="允许剪刀作为红石扳手", foreground="gray").grid(row=3, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # 性能优化 - 不发送无用实体数据包
        ttk.Label(config_frame, text="优化实体数据包:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.entity_packets_var = tk.BooleanVar()
        entity_packets_check = ttk.Checkbutton(config_frame, variable=self.entity_packets_var)
        entity_packets_check.grid(row=4, column=1, sticky=tk.W, pady=5)
        ttk.Label(config_frame, text="不发送无用的实体数据包", foreground="gray").grid(row=4, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # 性能优化 - 窒息优化
        ttk.Label(config_frame, text="窒息优化:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.suffocation_opt_var = tk.BooleanVar()
        suffocation_opt_check = ttk.Checkbutton(config_frame, variable=self.suffocation_opt_var)
        suffocation_opt_check.grid(row=5, column=1, sticky=tk.W, pady=5)
        ttk.Label(config_frame, text="启用窒息优化", foreground="gray").grid(row=5, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # 服务器语言
        ttk.Label(config_frame, text="服务器语言:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.server_lang_var = tk.StringVar()
        server_lang_combo = ttk.Combobox(config_frame, textvariable=self.server_lang_var, 
                                        values=["en_us", "zh_cn", "zh_tw"], width=10)
        server_lang_combo.grid(row=6, column=1, sticky=tk.W, pady=5)
        ttk.Label(config_frame, text="服务器语言设置", foreground="gray").grid(row=6, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # 服务器MOD名称
        ttk.Label(config_frame, text="服务器MOD名称:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.mod_name_var = tk.StringVar()
        mod_name_entry = ttk.Entry(config_frame, textvariable=self.mod_name_var, width=20)
        mod_name_entry.grid(row=7, column=1, sticky=tk.W, pady=5)
        ttk.Label(config_frame, text="服务器MOD显示名称", foreground="gray").grid(row=7, column=2, sticky=tk.W, padx=(10, 0), pady=5)
        
        # 按钮区域
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="加载配置", command=self.load_config).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="保存配置", command=self.save_config).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="重置", command=self.reset_config).pack(side=tk.LEFT, padx=(0, 10))
        
        # 状态栏
        self.status_var = tk.StringVar()
        self.status_var.set("就绪")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(10, 0))
        
        # 配置网格权重
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)
    
    def load_config(self):
        """加载配置文件"""
        try:
            if not os.path.exists(self.config_file):
                messagebox.showwarning("警告", f"配置文件 {self.config_file} 不存在，将使用默认值")
                self.reset_to_defaults()
                return
            
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config_data = yaml.safe_load(f) or {}
            
            # 更新界面
            self.update_ui_from_config()
            
            self.status_var.set(f"已加载配置: {self.config_file}")
        except Exception as e:
            messagebox.showerror("错误", f"加载配置文件时出错: {str(e)}")
            self.reset_to_defaults()
    
    def update_ui_from_config(self):
        """从配置数据更新界面"""
        try:
            # 自动更新
            auto_update_enable = self.get_nested_value(['settings', 'misc', 'auto-update', 'enable'], False)
            self.auto_update_var.set(bool(auto_update_enable))
            
            # 假人设置
            fakeplayer_enable = self.get_nested_value(['settings', 'modify', 'fakeplayer', 'enable'], False)
            self.fakeplayer_var.set(bool(fakeplayer_enable))
            
            fakeplayer_limit = self.get_nested_value(['settings', 'modify', 'fakeplayer', 'limit'], 10)
            self.fakeplayer_limit_var.set(str(fakeplayer_limit))
            
            # 红石剪刀扳手
            redstone_shears = self.get_nested_value(['settings', 'modify', 'redstone-shears-wrench'], True)
            self.redstone_shears_var.set(bool(redstone_shears))
            
            # 性能优化
            entity_packets = self.get_nested_value(['settings', 'performance', 'dont-send-useless-entity-packets'], True)
            self.entity_packets_var.set(bool(entity_packets))
            
            suffocation_opt = self.get_nested_value(['settings', 'performance', 'enable-suffocation-optimization'], True)
            self.suffocation_opt_var.set(bool(suffocation_opt))
            
            # 服务器语言
            server_lang = self.get_nested_value(['settings', 'misc', 'server-lang'], 'en_us')
            self.server_lang_var.set(str(server_lang) if server_lang else 'en_us')
            
            # MOD名称
            mod_name = self.get_nested_value(['settings', 'misc', 'server-mod-name'], 'Leaves')
            self.mod_name_var.set(str(mod_name) if mod_name else 'Leaves')
            
        except Exception as e:
            messagebox.showerror("错误", f"解析配置时出错: {str(e)}")
    
    def get_nested_value(self, keys, default=None):
        """获取嵌套字典中的值"""
        value = self.config_data
        try:
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
    
    def save_config(self):
        """保存配置到文件"""
        try:
            # 更新配置数据
            self.update_config_from_ui()
            
            # 保存到文件
            with open(self.config_file, 'w', encoding='utf-8') as f:
                yaml.dump(self.config_data, f, allow_unicode=True, indent=2, sort_keys=False, width=float("inf"))
            
            self.status_var.set(f"配置已保存到: {self.config_file}")
            messagebox.showinfo("成功", "配置已成功保存")
        except Exception as e:
            messagebox.showerror("错误", f"保存配置时出错: {str(e)}")
    
    def update_config_from_ui(self):
        """从界面更新配置数据"""
        # 确保必要的结构存在
        if 'settings' not in self.config_data:
            self.config_data['settings'] = {}
        if 'misc' not in self.config_data['settings']:
            self.config_data['settings']['misc'] = {}
        if 'auto-update' not in self.config_data['settings']['misc']:
            self.config_data['settings']['misc']['auto-update'] = {}
        if 'modify' not in self.config_data['settings']:
            self.config_data['settings']['modify'] = {}
        if 'fakeplayer' not in self.config_data['settings']['modify']:
            self.config_data['settings']['modify']['fakeplayer'] = {}
        if 'performance' not in self.config_data['settings']:
            self.config_data['settings']['performance'] = {}
        
        # 更新自动更新设置
        self.config_data['settings']['misc']['auto-update']['enable'] = self.auto_update_var.get()
        
        # 更新假人设置
        self.config_data['settings']['modify']['fakeplayer']['enable'] = self.fakeplayer_var.get()
        try:
            limit = int(self.fakeplayer_limit_var.get())
            self.config_data['settings']['modify']['fakeplayer']['limit'] = limit
        except ValueError:
            pass  # 保留原值
        
        # 更新红石剪刀扳手
        self.config_data['settings']['modify']['redstone-shears-wrench'] = self.redstone_shears_var.get()
        
        # 更新性能优化设置
        self.config_data['settings']['performance']['dont-send-useless-entity-packets'] = self.entity_packets_var.get()
        self.config_data['settings']['performance']['enable-suffocation-optimization'] = self.suffocation_opt_var.get()
        
        # 更新服务器语言和MOD名称
        self.config_data['settings']['misc']['server-lang'] = self.server_lang_var.get()
        self.config_data['settings']['misc']['server-mod-name'] = self.mod_name_var.get()
    
    def reset_config(self):
        """重置配置"""
        if messagebox.askyesno("确认", "确定要重置所有配置为默认值吗？"):
            self.reset_to_defaults()
            self.status_var.set("配置已重置为默认值")
    
    def reset_to_defaults(self):
        """重置为默认值"""
        self.auto_update_var.set(False)
        self.fakeplayer_var.set(False)
        self.fakeplayer_limit_var.set("10")
        self.redstone_shears_var.set(True)
        self.entity_packets_var.set(True)
        self.suffocation_opt_var.set(True)
        self.server_lang_var.set("en_us")
        self.mod_name_var.set("Leaves")

def main():
    root = tk.Tk()
    app = SimpleLeavesEditor(root)
    root.mainloop()

if __name__ == "__main__":
    main()