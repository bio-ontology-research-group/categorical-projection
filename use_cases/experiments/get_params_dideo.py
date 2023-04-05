with open("params_dideo.txt", "w") as f:
    for weight_decay in [0, 0.0001, 0.001]:
        for batch_size in [64, 128, 256]:
            for dim in [64, 128, 256]:
                for margin in [0,0.2, 0.4]:
                    f.write(f"{dim} {margin} {weight_decay} {batch_size}\n")


print("Done")
