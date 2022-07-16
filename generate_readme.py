import yaml
import os


table_divider = "|---|---|---|---|---|"
table_row = "| {} | {} | {} | {} | {} |"
table_head = table_row.format("Country", "Continent", "City, State", "Region", "S3 Endpoint")


def main():
    with open("README.md", "r") as f:
        original_readme = f.readlines()

    pruned_readme = []
    for line in original_readme:
        pruned_readme.append(line)
        if "BEGIN-GENERATION" in line:
            break

    for file in sorted(os.listdir("./data/")):
        if file.endswith(".yaml") and not file == "example.yaml":
            with open(os.path.join(".", "data", file)) as f:
                data = yaml.safe_load(f)

                pruned_readme.append("\n")
                pruned_readme.append(
                    f'## {data["provider"]["company"]} - {data["provider"]["service"]} - {data["provider"]["product"]}'
                )
                pruned_readme.append("\n")
                pruned_readme.append(table_head)
                pruned_readme.append("\n")
                pruned_readme.append(table_divider)
                pruned_readme.append("\n")
                for i in data["files"]:
                    obj = i["object"]
                    region = i["region"]

                    pruned_readme.append(
                        table_row.format(
                            region["country"],
                            region["continent"],
                            ", ".join([i for i in [region.get("city"), region.get("state")] if i]),
                            obj["region"],
                            obj.get("endpoint_url", ":question:"),
                        )
                    )
                    pruned_readme.append("\n")
    with open("README.md", "w") as f:
        f.writelines(pruned_readme)


if __name__ == "__main__":
    main()
