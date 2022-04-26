import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Iterator;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int cnt = 1;
        boolean isStackTrue = true;
        ArrayList<Integer> arrayList = new ArrayList<Integer>(n);
        ArrayList<String> result = new ArrayList<String>(n);
        for(int i = 0; i<n; i++){
            int num = Integer.parseInt(br.readLine());

            while(cnt <= num){
                arrayList.add(cnt);
                result.add("+");
                cnt++;
            }
            int g = arrayList.get(arrayList.size() - 1);
            if(num == g){

                result.add("-");

                arrayList.remove(arrayList.size() - 1);
            } else{
                isStackTrue = false;
            }
        }
        if(isStackTrue) {
            Iterator<String> it = result.iterator();
            while (it.hasNext()) {
                String s = it.next();
                System.out.println(s);
            }
        } else{
            System.out.println("NO");
        }
    }
}
