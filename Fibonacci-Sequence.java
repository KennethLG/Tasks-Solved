import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;

public class CodeAbbey{
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String strcase = bf.readLine();
        int cases = Integer.parseInt(strcase);
        String sal = "";
        for (int c = 0; c < cases; c++) {
            String strN = bf.readLine();
            BigInteger N = new BigInteger(strN);
            ArrayList<BigInteger> arr = new ArrayList<>();
            arr.add(BigInteger.ZERO);
            arr.add(BigInteger.ONE);
            
            for (int i = 2; i < 1000; i++) {
                BigInteger A = arr.get(i-1);
                BigInteger B = arr.get(i-2);
                arr.add(A.add(B));
                if (N.equals(arr.get(i))) {
                    sal += i + " ";
                }
            }
        }
        System.out.println(sal);
    }
}
