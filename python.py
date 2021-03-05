# Write csv file
def export_csv(ls, path=''):
    with open(path+'data_paragraph_classification.csv', 'w') as f:
        fieldnames = ['par', 'label']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for sample in ls:
            writer.writerow(sample)
