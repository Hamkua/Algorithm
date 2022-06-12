import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;


public class Main {
    static List<Integer> nodes = new ArrayList<>();
    static ArrayList<Integer> result = new ArrayList<>();
    static int size;

    public static void divide(int start, int end){
        if(start > end){
            return;
        }
        int mid = start;
        int p = nodes.get(start);
        result.add(0,p);
        for(int i = start + 1; i<=end; i++){
            if(p > nodes.get(i)){
                mid = i;
            }
        }

        divide(mid + 1, end);    //왜 이 둘의 순서에 따라 결과가 다른가?
        divide(start + 1, mid);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true){
            try {
                String input = br.readLine();
                if(input.equals("") || input == null){
                    break;
                }
                nodes.add(Integer.parseInt(input));
            }catch (Exception e){
                break;
            }

        }

        size = nodes.size();

        divide(0, size - 1);

        for(int i = 0; i<size; i++){
            System.out.println(result.get(i));
        }

        br.close();
    }
}
