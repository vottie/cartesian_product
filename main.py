# coding: utf-8

from lib.cartesian_product import CartesianProduct

def main():
    # Sample data
    arrays = [
        ["a", "b"],
        ["1", "2", "3"],
        ["@", "?"],
        ["A", "B", "C", "D"],
        ["000", "111", "123", "789", "0aje"],
        ["!", "#", "+"],
        ["91823", "kjk3", "lljk34"],
        [333, 444, 536, 921, 5150, 512350]
    ]

    # Create CartesianProduct instance
    cp = CartesianProduct()

    try:
        print("Processing with iterator:")
        # Display first 5 combinations using iterator
        for i, combination in enumerate(cp.iterate(arrays)):
            if i < 5:
                print(f"{i}: {combination}")
            else:
                print("...")
                break

        print("\nProcessing all combinations:")
        result = cp.execute(arrays)
        
        # Export results
        cp.to_csv(result, "output.csv")
        cp.to_json(result, "output.json")
        
        print(f"\nComplete: Generated {len(result)} combinations")
        print("Results have been saved to:")
        print("- output.csv")
        print("- output.json")

        print("\nFirst 5 results:")
        cp.display(result, limit=5)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
