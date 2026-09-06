[English](README_EN.md) | 中文

# GriddyCode
Coding has never been more lit!

https://github.com/face-hh/griddycode/assets/69168154/df93830e-6e24-472d-a854-cea026b12890

按 `CTRL` + `I` 在编辑器中查看快速介绍 :)

# 目录
   - [🍎 macOS 支持](#-macos-支持)
   - [环境要求](#环境要求)
   - [🚀 性能优化](#-性能优化)
   - [⌨️ Lua 扩展](#️-lua-扩展)
      - [路径](#路径)
      - [使用方法](#使用方法)
      - [文档](#文档)
         - [语言插件](#语言插件)
         - [主题](#主题)
      - [发布](#发布)
   - [贡献](#贡献)
      - [已知问题/待实现功能](#-已知问题待实现功能)

# 🍎 macOS 支持

本分支新增了完整的 macOS 支持，原项目仅支持 Windows 和 Linux。

## 下载
前往 [Releases](https://github.com/luohhua/griddycode/releases) 页面下载最新的 `.dmg` 文件，拖入 Applications 即可使用。

## 支持平台
- macOS 11.0+（Big Sur 及以上）
- Apple Silicon（M1/M2/M3/M4）原生支持
- Intel Mac 通过 Universal Binary 兼容

## 技术实现
- **Godot 4.4.1** — 支持原生 Metal 后端，未来可切换到 Metal 渲染获得更优性能
- **GL Compatibility 渲染器** — 当前使用 OpenGL，针对 2D 编辑器轻量高效
- **CI/CD 自动构建** — 推送 `v` 开头的 tag 自动编译 macOS DMG 并发布到 GitHub Releases
- **FiraCode Nerd Font** — 内置 Nerd Font 版本，文件图标完整显示
- **苹方 SC 字体** — 中文字体原生支持

## macOS 专属优化
| 优化项 | 说明 |
|--------|------|
| 字体渲染 | 关闭 MSDF，启用完整 hinting，文字锐利清晰 |
| 内存管理 | 延迟加载 23MB 表情字体，系统字体仅加载苹方 SC |
| 能效管理 | 低处理器模式 + 30fps 帧率限制，空闲时 GPU 完全休息 |
| 音频 | 24MB WAV 压缩为 3.2MB MP3，减少内存和磁盘占用 |
| 平台精简 | 删除未使用的 Linux/Windows/iOS 动态库，安装包更小 |

## 从源码构建
```bash
# 推送 tag 触发 GitHub Actions 自动构建
git tag v1.x.x
git push origin v1.x.x
# 构建完成后在 GitHub Releases 页面下载 DMG
```

# 环境要求
| 要求 | 说明 |
| -------- | -------- |
| [Nerd Font](https://www.nerdfonts.com/) — 文件选择器使用 Nerd Font 图标 | 如果图标显示为 "□" 说明缺少该字体 |

# 🚀 性能优化

本分支包含显著的性能和能效优化：

## GPU 与功耗
- **帧率限制 30fps** — 代码编辑器不需要 60fps，GPU 负载降低 50%
- **低处理器模式** — 画面不变时 Godot 跳过渲染，GPU 完全休息
- **着色器优化** — VHS/CRT 噪声函数简化（每像素 4 次计算 → 1 次）
- **Tween 泄漏修复** — camera.gd 不再每帧创建新的 tween
- **智能相机动画** — 仅在音乐播放时动画，否则静止

## 内存
- **表情符号字体延迟加载** — 23MB 的 NotoColorEmoji 仅在用户切换字体时加载
- **系统字体精简** — 只加载苹方 SC，不再加载 200+ 个系统字体
- **音频压缩** — 24MB WAV 转为 3.2MB MP3
- **清理无用平台二进制** — 删除未使用的 Linux/Windows/iOS 动态库（49MB → 12MB）
- **GL Compatibility 渲染器** — 比 Forward+ 更轻量，适合 2D 编辑器

## 渲染
- **Godot 4.4.1** — 最新稳定版，支持原生 Metal 后端
- **GL Compatibility 渲染器** — 针对 2D 代码编辑优化
- **字体清晰度** — 关闭 MSDF，启用完整 hinting，文字更锐利
- **光效优化** — HDR 阈值设为 0.45，平衡视觉效果与性能

## 优化指标
| 指标 | 优化前 | 优化后 |
|------|--------|--------|
| 内存占用 | 4.0 GB | ~1.1 GB |
| GPU 空闲状态 | 持续渲染 | 跳帧休息 |
| 帧率 | 无限制 | 30 FPS |
| 平台二进制 | 49 MB | 12 MB |
| 音频文件 | 24 MB WAV | 3.2 MB MP3 |

# ⌨️ Lua 扩展
GriddyCode 支持通过 **Lua** 扩展功能。

## 路径
Lua 脚本所在目录：

- Windows: `%APPDATA%\Godot\app_userdata\Bussin GriddyCode`
- macOS: `~/Library/Application Support/Bussin GriddyCode`
- Linux: `~/.local/share/godot/app_userdata/Bussin GriddyCode`

*注意：路径可能不完全准确，建议在系统的 AppData 中手动搜索 GriddyCode。*

## 使用方法
你会看到 **"langs"** 和 **"themes"** 两个文件夹：
- **"langs"** 存放 `.lua` 文件，用于语法高亮和自动补全
- **"themes"** 存放 `.lua` 文件，用于改变外观主题

*注意：Lua 脚本仅在切换不同文件扩展名时（如 "README.md" → "main.ts"）或重启 GriddyCode 后重新加载。*

## 文档
### 语言插件
#### 简介
为特定**文件扩展名**创建同名文件即可扩展功能（如 `toml.lua`）。

#### 方法

| 方法 | 示例 | 说明 | 备注 |
| -------- | -------- | -------- | -------- |
| `highlight(keyword: String, color: String)` | `highlight("const", "reserved")` | 用预设颜色高亮关键字 | 可用颜色：`reserved`、`annotation`、`string`、`binary`、`symbol`、`variable`、`operator`、`comments`、`error`、`function`、`member` |
| `highlight_region(start: String, end: String, color: String, line_only: bool = false)` | `highlight("/*", "*/", "comments", false)` | 高亮指定区域 | `start` 必须是符号，不支持正则 |
| `add_comment(comment: String)` | `add_comment("今天写什么代码呢 🗣️")` | 在 `CTRL` + `L` 菜单中添加随机评论 | 用户名、头像、日期和点赞数由 GriddyCode 自动生成 |
| `detect_functions(content: String, line: int, column: int) -> Array[String]` | `detect_functions("const test = 3; function main() {}")` | 输入时调用，结果显示在自动补全中 | 必须返回字符串数组，`line` 和 `column` 为光标位置 |
| `detect_variables(content: String, line: int, column: int) -> Array[String]` | `detect_variables("const test = 3;")` | 输入时调用，结果显示在自动补全中 | 必须返回字符串数组，`line` 和 `column` 为光标位置 |

*注意：要提供内置变量/函数（如 JS 的 `Math`/`parseInt()`），可以直接在返回的数组中预设，GriddyCode 会自动处理。*

### 主题
#### 简介
在 **"themes"** 文件夹中创建任意名称的文件即可添加主题（如 "dracula.lua"），之后可在 GriddyCode 中选择。

#### 方法
| 方法 | 示例 | 说明 | 备注 |
| -------- | -------- | -------- | -------- |
| `set_keywords(property: String, new_color: String)` | `set_keywords("reserved", "#ff00ff")` | 设置语法高亮颜色 | 第二个参数为十六进制颜色值，`#` 可选 |
| `set_gui(property: String, new_color: String)` | `set_gui("background_color", "#ff00ff")` | 设置 GUI 外观 | 可用属性：`background_color`、`current_line_color`、`selection_color`、`font_color`、`word_highlighted_color`、`selection_background_color` |
| `disable_glow()` | `disable_glow()` | 禁用光效 | Godot 的光效在浅色主题上可能导致全白，浅色主题建议添加此方法 |

*注意：如果输入的十六进制颜色无效，默认使用 #ff0000（红色）*

## 发布
如果只想**自己使用**主题/插件，放入 [AppData 路径](#路径) 即可。

如果想**提交**主题/插件，请提交 Pull Request，将文件添加到 `Lua/Plugins` 或 `Lua/Themes`。合并后将包含在下一个版本中。

# 贡献
非常欢迎贡献，无论是添加 Lua 插件、主题、安全地向 Lua 暴露更多功能，还是直接为 GriddyCode 添加功能！

## 注意事项
- 需要安装 [Godot Engine](https://godotengine.org/) 来运行和测试修改
- 不需要提交可执行文件
- 使用 v4.4.1 版本的引擎

## 🐛 已知问题/待实现功能：
### 高优先级
- `VHS & CRT` 着色器在某些主题（One Dark Pro、GitHub Light 等）下会完全变白，GitHub Dark 下正常
- 浅色模式受光效影响，深色模式正常

### 中优先级
- 在设置菜单（`CTRL` + `,`）中添加字体切换选项
- 当前行数限制约 1600 行，超过后 `CodeEdit` 节点会触发滚动导致相机异常

### 低优先级
- 设置菜单中的猫咪跳跃视频应随菜单淡入淡出
- `CTRL` + `P` 打开快速文件选择器（类似 VSCode）
- 选择带 "shader" 属性的设置时应禁用之前启用的着色器设置
- 每个设置场景的 `CheckButton` 节点不随主题变化（影响浅色主题）

请注意，提交 Pull Request 修复这些功能不保证会被合并。请确保代码质量后再提交。
