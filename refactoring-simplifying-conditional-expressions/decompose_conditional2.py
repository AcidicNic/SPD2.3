# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

def is_good_cholostrol(total_cholostrol, ldl, triglyceride):
    """Returns true if the cholestrol is in a good range."""
    return total_cholostrol < 200 and ldl < 100 and triglyceride < 150

def is_high_cholostrol(total_cholostrol, ldl, triglyceride):
    """Returns true if the cholestrol is too high."""
    return 200 < total_cholostrol > 240 or ldl > 160 or triglyceride >= 200

def is_low_cholostrol(total_cholostrol, ldl, triglyceride):
    """Returns true if the cholestrol is too low."""
    # i think this is low cholestrol? i don't know i'm not a doctor
    return 200 < total_cholostrol < 240 or 130 < ldl < 160 or \
                150 <= triglyceride < 200

def print_cholostrol_analysis(total_cholostrol, ldl, triglyceride):
    """Prints an analysis based on the given blood test data."""
    if is_good_cholostrol(total_cholostrol, ldl, triglyceride):
        print('*** Good level of cholestrol ***')
    elif is_high_cholostrol(total_cholostrol, ldl, triglyceride):
        print('*** High cholestrol level ***')
        print('start taking pills such as statins')
        print('start TLC diet')
    elif is_low_cholostrol(total_cholostrol, ldl, triglyceride):
        print('*** Borderline to moderately elevated ***')
        print('Start TLC diet')
        print('Under this meal plan, only 7 percent of your daily calories')
        print('should come from saturated fat.')
        print('Some foods help your digestive tract absorb less cholesterol.')
        print('For example, your doctor may encourage you to eat more:')
        print('oats, barley, and other whole grains.')
        print('fruits such as apples, pears, bananas, and oranges.')
    else:
        print('Error: unhandled case.')

if __name__ == '__main__':
    total_cholostrol = 70
    ldl = 30
    triglyceride = 120
    print_cholostrol_analysis(total_cholostrol, ldl, triglyceride)
