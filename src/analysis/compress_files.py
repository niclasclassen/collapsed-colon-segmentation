import os
import argparse
import SimpleITK as sitk


def parse_args():
    parser = argparse.ArgumentParser(
        description="compress .mha files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    required = parser.add_argument_group("required arguments")

    required.add_argument(
        "-i",
        "--input_dir",
        type=str,
        help="Define directory containing files in .mha format.",
        required=True,
    )

    required.add_argument(
        "-o",
        "--output_dir",
        type=str,
        default="segmentations_variability.csv",
        help="Define output dir for compressed files.",
    )

    return parser.parse_args()


def main():
    # load args
    args = parse_args()

    # Iterate over all .mha files in the folder
    for filename in sorted(os.listdir(args.input_dir)):
        print("Processing file:", filename, flush=True)
        try:
            if filename.endswith(".mha"):
                filepath = os.path.join(args.input_dir, filename)

                # Read the .mha file
                image = sitk.ReadImage(filepath)

                # Write compressed file
                sitk.WriteImage(
                    image, f"{args.output_dir}{filename}", useCompression=True
                )
        except Exception as e:
            print(e)

    print(f"Finished compression of files.")


if __name__ == "__main__":
    main()
