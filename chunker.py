def split_into_chunks(filename, chunk_size):
    with open(filename, "r") as f:
        lines = f.readlines()

    chunks = []
    for i in range(0, len(lines), chunk_size):
        chunks.append(lines[i:i + chunk_size])

    return chunks