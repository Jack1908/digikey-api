# DigiKey 元器件搜索工具

这是一个用于通过 DigiKey API 搜索电子元器件的 Python 工具。支持关键词搜索、零件号搜索和批量搜索，并可以将结果保存为 CSV 文件。

## 功能特点
- **关键词搜索**：通过关键词搜索元器件。
- **零件号搜索**：通过 DigiKey 零件号获取详细信息。
- **批量搜索**：从 CSV 文件中批量查询多个零件号。
- **CSV 导出**：将搜索结果保存为 CSV 文件。
- **错误处理**：完整的错误处理和日志记录。

## 安装要求
- Python 3.7 或更高版本
- `digikey-api` Python 包
- `pyyaml` Python 包

## 安装步骤
1. 克隆或下载此仓库。
2. 安装依赖包：
   ```bash
   pip install digikey-api pyyaml
   ```
3. 配置 `config.yaml` 文件：
   ```yaml
   digikey:
     client_id: "your_client_id_here"  # 您的 DigiKey Client ID
     client_secret: "your_client_secret_here"  # 您的 DigiKey Client Secret
     sandbox: "false"  # 设置为 false 以使用生产环境
   ```

## 使用方法
### 1. 关键词搜索
```bash
python search_components.py --keyword "STM32" --count 5
```

### 2. 零件号搜索
```bash
python search_components.py --part-number "STM32F103C8T6-ND"
```

### 3. 批量搜索
创建一个包含零件号的 CSV 文件（例如 `part_numbers.csv`），格式如下：
```csv
Part Number
STM32F103C8T6-ND
STM32F103RBT6-ND
```

然后运行：
```bash
python search_components.py --input-csv part_numbers.csv --csv --output results.csv
```

### 4. 保存结果到 CSV
使用 `--csv` 参数将搜索结果保存为 CSV 文件：
```bash
python search_components.py --keyword "STM32" --csv --output results.csv
```

## 注意事项
1. 确保您的 DigiKey API 凭证有效。
2. 首次使用时会自动创建 `.digikey_storage` 目录用于存储认证信息。
3. 如果遇到 SSL 证书验证问题，请确保您的系统时间准确。

## 许可证
MIT License