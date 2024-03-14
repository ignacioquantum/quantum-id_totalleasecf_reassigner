from id_totalleasecf_reassigner import IdTotalLeaseCfReassigner


def main():
    # Tu código principal va aquí
    ids_to_check = [520]

    for id in ids_to_check:
        driver = IdTotalLeaseCfReassigner(id)
        driver.main()

if __name__ == "__main__":
    main()