import math
import ti_system

# Retrieve the current Ans value from the calculator OS
try:
    ans_val = float(ti_system.recall_value("Ans"))
except Exception:
    ans_val = 0.0

print("Default X =", ans_val)
user_in = input("Value for X or [0 for default]: ")

# Parse user input
try:
    x_val = float(user_in)
except ValueError:
    x_val = 0.0

# Use Ans if the user entered 0
if x_val == 0.0:
    x_val = ans_val

# Initialize continued fraction variables
scaled_val = x_val / math.pi
num_curr = 1
num_prev = 0
den_curr = 0
den_prev = 1
remainder = scaled_val

# Calculate the fraction
while True:
    if den_curr > 0:
        if abs(scaled_val - (num_curr / den_curr)) < 0.000001 or den_curr > 1000:
            break

    # iPart is equivalent to int() in Python
    integer_part = int(remainder)
    
    next_num = num_curr * integer_part + num_prev
    next_den = den_curr * integer_part + den_prev

    num_prev = num_curr
    den_prev = den_curr
    num_curr = next_num
    den_curr = next_den

    # fPart is the remainder minus its integer part
    f_part = remainder - integer_part
    
    # Avoid division by zero if there's no fractional part left
    if f_part == 0 or abs(f_part) < 1e-12:
        break

    remainder = 1 / f_part

# Display the results matching the requested format
print("X =", x_val)
print("PI Ratio: " + str(num_curr) + "pi/" + str(den_curr))