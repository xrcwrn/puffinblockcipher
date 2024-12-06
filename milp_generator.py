def generate_puffin_milp():
    num_sboxes = 16  # Total S-boxes
    sbox_size = 4    # Number of input/output bits per S-box
    constraints = []

    # Objective Function
    objective = "Minimize\n    " + " + ".join([f"a{i:02d}" for i in range(num_sboxes)]) + "\n"
    constraints.append(objective)

    # Global Activity Constraint
    global_activity = "Subject To\n    R0: " + " + ".join(
        [f"x{i:02d}{j}" for i in range(num_sboxes) for j in range(sbox_size)]
    ) + " >= 1\n"
    constraints.append(global_activity)

    # S-box Constraints
    row_index = 1
    for i in range(num_sboxes):
        input_bits = [f"x{i:02d}{j}" for j in range(sbox_size)]
        output_bits = [f"x1{i:02d}{j}" for j in range(sbox_size)]
        a_var = f"a{i:02d}"

        # Input activity constraints
        for j in range(sbox_size):
            constraints.append(f"    R{row_index}: {input_bits[j]} - {a_var} <= 0\n")
            row_index += 1

        # Sum of input constraints
        constraints.append(
            f"    R{row_index}: " +
            " + ".join(input_bits) +
            f" - {a_var} >= 0\n"
        )
        row_index += 1

        # Propagation constraints
        constraints.append(
            f"    R{row_index}: 4 " +
            " + 4 ".join(output_bits) +
            " - " +
            " - ".join(input_bits) +
            " >= 0\n"
        )
        row_index += 1

        constraints.append(
            f"    R{row_index}: 4 " +
            " + 4 ".join(input_bits) +
            " - " +
            " - ".join(output_bits) +
            " >= 0\n"
        )
        row_index += 1

        # Total activity constraint
        constraints.append(
            f"    R{row_index}: " +
            " + ".join(input_bits + output_bits) +
            f" - 3{a_var} >= 0\n"
        )
        row_index += 1

    # Bounds Section
    bounds = "Bounds\n"
    for i in range(num_sboxes):
        for j in range(sbox_size):
            bounds += f"    0 <= x{i:02d}{j}\n"
        bounds += f"    0 <= a{i:02d}\n"

    # Binary Variables
    binary_vars = "Binary\n    " + ", ".join(
        [f"x{i:02d}{j}" for i in range(num_sboxes) for j in range(sbox_size)]
    ) + "\n"

    # General Variables
    generals = "Generals\n    " + ", ".join([f"a{i:02d}" for i in range(num_sboxes)]) + "\n"

    # End Statement
    end = "End\n"

    # Combine all constraints
    milp_code = "".join(constraints) + bounds + binary_vars + generals + end
    return milp_code


# Generate MILP
milp_code = generate_puffin_milp()

# Print the generated MILP code
print(milp_code)

# Optionally, save to a file
with open("puffin_milp.lp", "w") as file:
    file.write(milp_code)
