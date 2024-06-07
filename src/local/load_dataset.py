def load_data_sql(data_dir: str = "data_sql"):
    from datasets import load_dataset

    dataset = load_dataset("b-mc2/sql-create-context")

    dataset_splits = {"train": dataset["train"]}

load_data_sql()