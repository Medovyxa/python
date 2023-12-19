import argparse
import csv
import logging
import os


def create_annotation_file(folder_path: str, subfolder_paths: list, dest_folder_path: str):
    """
    the function creates a csv file
    Parameters
    ----------
    folder_path : str
    subfolder_paths : list
    annotation_file_path : str
    """
    try:
        zebra_annotation_file = os.path.join(folder_path, 'zebra_annotation.csv')
        bayhorse_annotation_file = os.path.join(folder_path, 'bayhorse_annotation.csv')

        with open(zebra_annotation_file, 'w', newline='') as zebra_csvfile:
            zebra_csv_writer = csv.writer(zebra_csvfile)
            zebra_csv_writer.writerow(['The absolute path', 'relative path', 'the text name of the class'])

            with open(bayhorse_annotation_file, 'w', newline='') as bayhorse_csvfile:
                bayhorse_csv_writer = csv.writer(bayhorse_csvfile)
                bayhorse_csv_writer.writerow(['The absolute path', 'relative path', 'the text name of the class'])

                for subfolder_path in subfolder_paths:
                    if os.path.isdir(os.path.join(folder_path, subfolder_path)):
                        class_name = os.path.basename(subfolder_path)

                        for filename in os.listdir(os.path.join(folder_path, subfolder_path)):
                            absolute_path = os.path.join(folder_path, subfolder_path, filename)
                            relative_path = os.path.join(subfolder_path, filename)

                            if class_name == 'zebra':
                                zebra_csv_writer.writerow([absolute_path, relative_path, class_name])
                            elif class_name == 'bayhorse':
                                bayhorse_csv_writer.writerow([absolute_path, relative_path, class_name])

        logging.info(f"The files with the annotations for cat and dog have been created.")
    except Exception as e:
        logging.exception(f"Error in creating annotation files: {e}")




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create annotation file for the dataset')
    parser.add_argument('folder_path', type=str, default='dataset', help='Path to the dataset directory')
    parser.add_argument('subfolder_paths', nargs='+', type=str, help='List of subfolder paths')
    parser.add_argument('annotation_file', type=str, default='annotation.csv', help='Path for the annotation file')

    args = parser.parse_args()
    create_annotation_file(args.folder_path, args.subfolder_paths, args.annotation_file)