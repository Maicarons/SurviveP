#!/usr/bin/env python3
import os
import re

def scan_plugins():
    """扫描plugins目录第一层的所有.jar和.jar[disabled]文件"""
    plugins_dir = '../plugins'
    plugin_files = []
    
    # 只遍历plugins目录的第一层
    for item in os.listdir(plugins_dir):
        item_path = os.path.join(plugins_dir, item)
        # 检查是否为文件且匹配.jar和.jar[disabled]模式
        if os.path.isfile(item_path) and re.match(r'.*\.jar(\[disabled\])?$', item):
            plugin_files.append(item)
    
    return sorted(plugin_files)

def generate_markdown(plugins):
    """生成markdown格式的插件列表"""
    md_content = "# 插件列表\n\n"
    md_content += "| 序号 | 插件名称 | 状态 |\n"
    md_content += "|------|----------|------|\n"
    
    for i, plugin in enumerate(plugins, 1):
        # 判断是否为禁用状态
        status = "已禁用" if plugin.endswith('[disabled]') else "启用中"
        # 移除状态后缀以获得干净的名称
        clean_name = plugin[:-10] if plugin.endswith('[disabled]') else plugin
        md_content += f"| {i} | {clean_name} | {status} |\n"
    
    return md_content

def write_markdown(content):
    """将markdown内容写入文件"""
    with open('../plugin_list.md', 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    """主函数"""
    print("正在扫描插件...")
    plugins = scan_plugins()
    print(f"找到 {len(plugins)} 个插件")
    
    print("生成插件列表...")
    md_content = generate_markdown(plugins)
    
    print("写入plugin.md文件...")
    write_markdown(md_content)
    
    print("完成！")

if __name__ == "__main__":
    main()