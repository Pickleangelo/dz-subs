import os

def convert_srt_to_vtt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    vtt_lines = ['WEBVTT\n\n']
    skip_number = True

    for line in lines:
        stripped = line.strip()

        # Skip numeric subtitle sequence lines like "1", "2", "3", etc.
        if skip_number and stripped.isdigit():
            continue

        # Once a timestamp line is hit, stop skipping numeric checks
        if '-->' in line:
            skip_number = False
            line = line.replace(',', '.')
            vtt_lines.append(line)
        elif stripped == "":
            skip_number = True
            vtt_lines.append("\n")
        else:
            vtt_lines.append(line)

    vtt_path = file_path[:-4] + '.vtt'
    with open(vtt_path, 'w', encoding='utf-8') as f:
        f.writelines(vtt_lines)

    os.remove(file_path)
    print(f"Converted and deleted: {file_path}")

if __name__ == '__main__':
    for filename in os.listdir():
        if filename.lower().endswith('.srt'):
            convert_srt_to_vtt(filename)
