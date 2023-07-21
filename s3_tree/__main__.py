import typer
from s3_tree import s3_tree
import boto3
import os
from typing import Annotated

app = typer.Typer(add_completion=True)


@app.command()
def main(profile_name: Annotated[str, typer.Argument(help="AWS profile name")],
           bucket_name: Annotated[str, typer.Argument(help="Bucket name")],
           prefix: Annotated[str, typer.Argument(help="Prefix to filter")],
           max_depth: Annotated[int, typer.Argument(help="Max depth to traverse")] = 3,
           show_files: Annotated[bool, typer.Argument(help="Show files or not")]= False,
           max_files_to_show: Annotated[int, typer.Argument(help="If show, how many files to show")] = 10,
           verbose: Annotated[bool, typer.Argument(help="Verbose or not")] = False):
    """
    Prints all files in a S3 bucket as a tree.
    """
    session = boto3.Session(profile_name=profile_name)
    s3 = session.client('s3')

    container = s3_tree.core(bucket_name,
                        prefix,
                        max_depth=max_depth,
                        show_files=show_files,
                        max_files_to_show=max_files_to_show,
                        verbose=verbose,
                        client=s3
                        )

    with open('/tmp/s3_tree.txt', 'w') as f:
        for item in container:
            f.write("%s\n" % item)
    # run a command on os shell
    os.system('tree --fromfile /tmp/s3_tree.txt')


if __name__ == '__main__':
    app()
