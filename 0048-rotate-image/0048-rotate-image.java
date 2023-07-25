class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        int[][] ans = new int[n][n];
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix.length;j++){
                ans[j][(n-1)-i] = matrix[i][j];
            }
        }
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix.length;j++){
                matrix[i][j] = ans[i][j];
            }
        }
    }
}