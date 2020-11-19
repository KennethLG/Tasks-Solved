import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class CodeAbbey{
    static BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    public static void main(String[] args) throws IOException{
        String strcases = bf.readLine();
        String sal = "";
        char[] L = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'};
        for (int c = 0; c < (Integer.parseInt(strcases)); c++) {
            String line = bf.readLine();
            int Kx=0;int Qx=0;
            int Ky = Integer.parseInt(String.valueOf(line.charAt(1)));
            int Qy = Integer.parseInt(String.valueOf(line.charAt(4)));
            for (int ch = 0; ch < L.length; ch++) {
                if (L[ch] == line.charAt(0)) {
                    Kx = ch+1;
                }
                if (L[ch] == line.charAt(3)) {
                    Qx = ch+1;
                }
            }
            // comprobacion horizontal y vertical
            if (Kx == Qx || Ky == Qy) {
                sal += "Y ";
            } else { // comprobacion diagonal == puto dolor de bolas
                if ((Math.abs(Qx - Kx)) == (Math.abs(Qy - Ky))) {
                    sal += "Y ";
                } else {
                    sal += "N ";
                }
            }
        }
        System.out.println(sal);
    }
}
