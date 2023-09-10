for i in range(1,21):
    with open(f"Tables/Multiplivcation_Table_Of_{i}",'w') as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}")
            if j!=10:
                f.write("\n")