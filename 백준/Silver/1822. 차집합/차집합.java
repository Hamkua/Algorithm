import java.util.*;
import java.io.*;
public class Main {
    static BufferedReader br;
    static StringTokenizer st;
    static StringBuilder sb;
    static int N,M;
    static int []arr;
    static int []arr2;
    public static void main(String[]args) throws IOException{
        input();
        logic();
    }
    static void input() throws IOException{
        br=new BufferedReader(new InputStreamReader(System.in));
        sb=new StringBuilder();
        st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        arr=new int [N];
        arr2=new int [M];
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<M;i++){
            arr2[i]=Integer.parseInt(st.nextToken());
        }
    }
    static void logic(){
        Arrays.sort(arr);
        Arrays.sort(arr2);
        int C=0;
        for(int i=0;i<N;i++){
            int Cnt=binarySearch(arr2,0,M-1,arr[i]);
            if(Cnt==0){
                C++;
                sb.append(arr[i]).append(" ");
            }
        }
        System.out.println(C);
        if(C > 0){
            System.out.println(sb);
        }
    }
    static int binarySearch(int[] arr, int L, int R, int X) {
        while (L <= R) {
            int mid = (L + R) / 2;
            if (arr[mid] == X) {
                return 1;
            } else if (arr[mid] < X) {
                L = mid + 1;
            } else if (arr[mid] > X){
                R = mid - 1;
            }
        }
        return 0;
    }
}