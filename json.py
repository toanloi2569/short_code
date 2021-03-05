def pretty_print_json(row):
    print(json.dumps(
        row,
        indent=4,
        separators=(',', ': '),
        ensure_ascii=False
    ).encode('utf8').decode())
