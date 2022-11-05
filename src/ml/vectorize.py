import pandas as pd


def read_file_to_df(filename):
    objects = []
    with open(filename) as f:
        for line in f:
            objects.append(line.split())

    df_objects = pd.DataFrame(objects)
    df_objects = df_objects.rename(columns={0: "class_name",
                                            1: "class_id",
                                            2: "x_center",
                                            3: "y_center",
                                            4: "width",
                                            5: "height",
                                            6: "frame"})
    return df_objects


def calculate_vector(p1, p2):
    return (p2[0] - p1[0], p2[1] - p1[1])


def get_direction(vector, threshold=0):
    if vector[1] == 0:
        return None
    elif vector[1] < threshold:
        return 1
    return -1

    return vector[1] < threshold  # 1 insert, 0 remove


def get_final_direction(df):
    vector = calculate_vector([df.x_center.iloc[0], df.y_center.iloc[0]], [df.x_center.iloc[-1], df.y_center.iloc[-1]])
    direction = get_direction(vector)
    return direction


def main():
    file_path = './src/ml/runs/detect/exp/labels/result.txt'
    df_objects = read_file_to_df(file_path)
    df_objects = df_objects.astype({'x_center': 'float', 'y_center': 'float'})

    unique_classes = df_objects.class_id.unique()

    dest_path = './direction_result.csv'
    with open(dest_path, 'w') as f:
        for unique in unique_classes:
            direction = get_final_direction(df_objects[df_objects.class_id == unique])
            f.write(unique + ',' + str(direction) + '\n')


if __name__ == "__main__":
    main()
