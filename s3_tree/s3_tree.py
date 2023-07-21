container = []


def core(bucket_name, prefix, max_depth=3, show_files=False, max_files_to_show=10, verbose=False, client=None):
    global container
    # get the files inside the bucket
    response = client.list_objects_v2(Bucket=bucket_name,
                                      Prefix=prefix,
                                      Delimiter='/')
    print(f"Prefix: {prefix}") if verbose else None
    folders = response.get('CommonPrefixes')

    if folders is not None:
        for f in folders:
            # get the folder name
            folder = f.get('Prefix')
            print(f"Folder: {folder}") if verbose else None
            container.append(folder)
            # compute number of delimiters in the folder name
            current_depth = folder.count('/')
            print(f"Current depth: {current_depth}") if verbose else None
            if current_depth <= max_depth:
                core(bucket_name,
                     folder,
                     show_files=show_files,
                     max_depth=max_depth,
                     max_files_to_show=max_files_to_show,
                     verbose=verbose,
                     client=client)
            else:
                print("Max depth reached") if verbose else None
    else:
        if show_files:
            # get the Contents
            for i, c in enumerate(response.get('Contents')):
                print(f"File: {c.get('Key')}") if verbose else None
                container.append(c.get('Key'))
                if i >= max_files_to_show:
                    break
    return container
