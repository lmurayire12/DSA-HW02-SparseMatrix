class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = {}

    def set_element(self, row, col, value):
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of bounds")
        if value != 0:
            self.matrix[(row, col)] = value

    def get_element(self, row, col):
        if row >= self.rows or col >= self.cols:
            raise IndexError("Index out of bounds")
        return self.matrix.get((row, col), 0)

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = SparseMatrix(self.rows, self.cols)
        for (i, j), value in self.matrix.items():
            result.set_element(i, j, value)
        for (i, j), value in other.matrix.items():
            result.set_element(i, j, result.get_element(i, j) + value)
        return result

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = SparseMatrix(self.rows, self.cols)
        for (i, j), value in self.matrix.items():
            result.set_element(i, j, value)
        for (i, j), value in other.matrix.items():
            result.set_element(i, j, result.get_element(i, j) - value)
        return result

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix for multiplication")
        result = SparseMatrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                dot_product = sum(self.get_element(i, k) * other.get_element(k, j) for k in range(self.cols))
                result.set_element(i, j, dot_product)
        return result

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            # Read the number of rows and columns
            rows = int(file.readline().split('=')[1])
            cols = int(file.readline().split('=')[1])

            # Initialize the matrix
            matrix = cls(rows, cols)

            # Read and set matrix elements
            for line in file:
                if line.strip():
                    # Parse the line to get row, column, and value
                    row, col, value = map(int, line.strip()[1:-1].split(','))
                    # Print the indices for debugging
                    print("Row:", row, "Col:", col)
                    # Check if the indices are within bounds
                    if row >= rows or col >= cols:
                        raise IndexError("Index out of bounds")
                    # Set the element in the matrix
                    matrix.set_element(row, col, value)

        return matrix




def main():
    print("Enter path to first matrix file:")
    file_path1 = input()
    matrix1 = SparseMatrix.from_file(file_path1)
    print("Enter path to second matrix file:")
    file_path2 = input()
    matrix2 = SparseMatrix.from_file(file_path2)

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = int(input())
    
    if choice == 1:
        result = matrix1.add(matrix2)
    elif choice == 2:
        result = matrix1.subtract(matrix2)
    elif choice == 3:
        result = matrix1.multiply(matrix2)
    else:
        print("Invalid choice")
        return

    print("Result:")
    for i in range(result.rows):
        for j in range(result.cols):
            print(result.get_element(i, j), end=" ")
        print()

if __name__ == "__main__":
    main()

