import os
import csv
import json
import argparse


def search_keywords_in_csv(file_path, keywords):
    """
    Search for keywords in a CSV file.

    Args:
        file_path (str): Path to the CSV file.
        keywords (list): List of keywords to search for.

    Returns:
        list: A list of dictionaries containing results.
    """
    results = []

    # Read the CSV file
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            for field, value in row.items():
                if value and any(keyword.lower() in value.lower() for keyword in keywords):
                    results.append({"file": os.path.basename(file_path), "row": row, "keyword": value})
                    break  # Stop checking other fields in the same row

    return results


def process_path(path, keywords):
    """
    Process a path (file or folder) to search keywords in CSV files.

    Args:
        path (str): Path to a file or folder.
        keywords (list): List of keywords to search for.

    Returns:
        list: A list of dictionaries containing all results from the files.
    """
    all_results = []

    if os.path.isfile(path):
        # Single file
        if path.lower().endswith(".csv"):
            all_results.extend(search_keywords_in_csv(path, keywords))
    elif os.path.isdir(path):
        # Folder containing multiple files
        for root, _, files in os.walk(path):
            for file_name in files:
                if file_name.lower().endswith(".csv"):
                    file_path = os.path.join(root, file_name)
                    all_results.extend(search_keywords_in_csv(file_path, keywords))
    else:
        raise ValueError(f"The path '{path}' is neither a file nor a folder.")

    return all_results


def save_results(results, output_format, output_file):
    """
    Save results to the specified output format.

    Args:
        results (list): List of results to save.
        output_format (str): Format of the output file (txt, csv, json).
        output_file (str): Path to the output file.
    """
    if output_format == "txt":
        with open(output_file, 'w', encoding='utf-8') as txt_file:
            for result in results:
                txt_file.write(f"Found in: {result['file']} | Keyword: {result['keyword']} | Row: {result['row']}\n")

    elif output_format == "csv":
        # Dynamically create fieldnames
        all_fieldnames = set()
        for result in results:
            all_fieldnames.update(result["row"].keys())
        fieldnames = ["file", "keyword"] + list(all_fieldnames)

        # Write to CSV
        with open(output_file, 'w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for result in results:
                row_data = {"file": result["file"], "keyword": result["keyword"]}
                row_data.update(result["row"])
                csv_writer.writerow(row_data)

    elif output_format == "json":
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(results, json_file, indent=4, ensure_ascii=False)

def main():
    parser = argparse.ArgumentParser(description="Search for keywords in CSV files.")
    parser.add_argument("--path", required=True, help="Path to a CSV file or folder containing CSV files.")
    parser.add_argument("--keyword", required=True, help="Comma-separated keywords to search for.")
    parser.add_argument("--output", required=True, help="Path to the output file (supports txt, csv, json).")
    args = parser.parse_args()

    # Parse keywords
    keywords = [keyword.strip() for keyword in args.keyword.split(",")]

    # Get the output format
    output_format = os.path.splitext(args.output)[1].lower().lstrip(".")

    # Validate output format
    if output_format not in ["txt", "csv", "json"]:
        raise ValueError("Output format must be one of: txt, csv, json")

    # Process the path
    results = process_path(args.path, keywords)

    # Save the results
    if results:
        save_results(results, output_format, args.output)
        print(f"Results saved to {args.output}")
    else:
        print("No matching keywords found.")


if __name__ == "__main__":
    main()
