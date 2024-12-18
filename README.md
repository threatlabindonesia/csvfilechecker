# Keyword Search in CSV Files

This script is a powerful utility for searching specific keywords within CSV files or directories containing CSV files. It allows you to efficiently locate and extract relevant rows based on your search criteria and save the results in your desired format.

---

## Features

- **Search keywords in CSV files**: Locate specific keywords within rows of CSV files.
- **Support for single files or directories**: Process individual CSV files or scan entire directories.
- **Flexible output formats**: Save results in `txt`, `csv`, or `json` format.
- **Dynamic field handling**: Automatically extracts and handles fields in CSV rows.
- **Easy-to-use CLI interface**: Specify paths, keywords, and output details directly from the command line.

---

## Requirements

- Python 3.6 or later
- Modules: `os`, `csv`, `json`, `argparse`

---

## Installation

1. Clone or download the repository.
2. Ensure Python is installed on your machine.
3. Install any necessary dependencies (if not included in your environment).

---

## Usage

The script is executed via the command line. Use the following format:

```bash
python checkContentCsv.py --path <path_to_file_or_directory> --keyword <comma_separated_keywords> --output <output_file_with_extension>
```

### Arguments

- `--path`: Path to the CSV file or folder containing CSV files to process.
- `--keyword`: Comma-separated list of keywords to search for (case-insensitive).
- `--output`: Path to the output file. Supports `.txt`, `.csv`, or `.json` formats.

---

### Examples

1. **Search a single CSV file**:
   ```bash
   python checkContentCsv.py --path data.csv --keyword "error,warning" --output results.json
   ```

2. **Search all CSV files in a directory**:
   ```bash
   python checkContentCsv.py --path ./data --keyword "critical,failure" --output output.csv
   ```

3. **Save results in a text file**:
   ```bash
   python checkContentCsv.py --path ./data --keyword "info,debug" --output output.txt
   ```

---

## Output Formats

### TXT
The results are saved in a human-readable format:
```
Found in: example.csv | Keyword: warning | Row: {'id': '1', 'status': 'warning', 'message': 'Disk space low'}
```

### CSV
The results are saved as a CSV file with fields dynamically extracted from the input file(s).

### JSON
The results are saved in structured JSON format:
```json
[
    {
        "file": "example.csv",
        "keyword": "error",
        "row": {
            "id": "2",
            "status": "error",
            "message": "File not found"
        }
    }
]
```

---

## Error Handling

- If the provided path does not exist or is invalid, the script will raise a `ValueError`.
- Only files with `.csv` extensions are processed.
- Output format must be one of: `txt`, `csv`, `json`. Otherwise, a `ValueError` is raised.

---

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance functionality or improve the code.

---

## License

This project is open-source and available under the MIT License.

---

## Author
- **Afif Hidayatullah**
- Organization: ITSEC Asia
- Contact: [Linkedin](https://www.linkedin.com/in/afif-hidayatullah/)
Feel free to reach out for any questions or support regarding this tool!

---

Happy searching! 😊
