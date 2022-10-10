public class magicSquare{
    public static void main(){
        int n=3;
        generateMatrix(n);
    }
    static void generateMatrix(int n){
        int[][] magicSqare = new int [n][n];
        // intitial positions of the value  1
        int i=n%n;
        int j=n/2;
        for (int k=1;k<n*n;k++){
            if(i==-1 & j==n){
                j=n-1;
                i=0;
            }
            // restricting number going out of the box
            else{
                if(j==n){
                    j=0;
                }
                if(i<0){
                    i=n-1;
                }
            }

            if(magicSqare[i][j]!=0){
                j-=2;
                i++;
                continue;
            }
            else{
                magicSqare[i][j]=k++;
            }
            j++;
            i--;
        }

        for(int k=0;k<n;k++){
            for(int l=0;l<n;l++){
                System.out.print(magicSqare[k][l]);
                System.out.println();
            }
        }
    }
}