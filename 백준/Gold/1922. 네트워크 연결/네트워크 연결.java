import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, m, a, b, edge;
    static StringTokenizer st;
    static List<CostInfo>[] data;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        data = new List[n + 1];
        for(int i = 0; i <= n; i++){
            data[i] = new LinkedList<CostInfo>();
        }

        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());

            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            edge = Integer.parseInt(st.nextToken());

            data[a].add(new CostInfo(edge, b));
            data[b].add(new CostInfo(edge, a));
        }

        System.out.println(prim());
    }

    public static int prim(){
        int[] visited = new int[n + 1];
        Arrays.fill(visited, 0);
        visited[1] = 1;

        PriorityQueue<CostInfo> pq = new PriorityQueue<>();

        int result = 0;

        for(CostInfo costInfo : data[1]){
            pq.add(costInfo);
        }

        while(!pq.isEmpty()){
//            Iterator<CostInfo> it = pq.iterator();
//            while(it.hasNext()){
//                CostInfo next = it.next();
//
//                System.out.print("(" + next.edge + ", " + next.destination + "), ");
//            }
//            System.out.println();

            CostInfo costInfo = pq.poll();
            int destination = costInfo.destination;
            int edge = costInfo.edge;


            if(visited[destination] == 0){
                visited[destination] = 1;
//                System.out.println(destination + ", " + edge);
                result += edge;
                for(CostInfo costInfo1 : data[destination]){
                    pq.add(costInfo1);
                }
            }

            int sum = 0;
            for(int n : visited){
                sum += n;
            }

            if(sum == n){
                return result;
            }
        }

        return result;
    }

    static class CostInfo implements Comparable<CostInfo>{
        int edge, destination;

        public CostInfo(int edge, int destination){
            this.edge = edge;
            this.destination = destination;
        }

        @Override
        public int compareTo(CostInfo costInfo) {
            if(this.edge < costInfo.edge){
                return -1;
            }else{
                return 1;
            }
        }
    }
}
