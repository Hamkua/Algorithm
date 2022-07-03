import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static LinkedList<Node>[] data;
    static PriorityQueue<Node> pq = new PriorityQueue<>();
    static int[] result;
    static final int INF = Integer.MAX_VALUE;
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int testCase = Integer.parseInt(br.readLine());

        for(int t = 0; t<testCase; t++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            data = new LinkedList[n + 1];
            for(int i = 1; i<=n; i++){
                data[i] = new LinkedList<>();
            }

            //setall의 매개변수로 람다식을 사용 -> 외부 이터레이터를 사용하여 성능 저하된다고 함

            result = new int[n+1];
            Arrays.fill(result, INF);
            result[c] = 0;



            for(int i = 0; i<d; i++){
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int s = Integer.parseInt(st.nextToken());

                data[b].add(new Node(s, a));
            }

            dijkstra(c);
            int cnt = 0;
            int maxVal = 0;

            for(int i = 1; i <= n; i++){
                if(result[i] != INF){
                    cnt++;
                    if(result[i] > maxVal){
                        maxVal = result[i];
                    }
                }
            }

            System.out.println(cnt + " " + maxVal);
        }

        br.close();
    }


    static void dijkstra(int start){
        pq.add(new Node(0, start));

        while(!pq.isEmpty()){
            Node pop = pq.poll();
            int e = pop.getEdge();
            int v = pop.getValue();

            Iterator<Node> it = data[v].iterator();
            while(it.hasNext()){
                Node nextNode = it.next();

                if(nextNode.getEdge() != INF) {
                    int nextEdge = nextNode.getEdge() + e;
                    int nextVal = nextNode.getValue();
                    if (result[nextVal] > nextEdge) {

                        result[nextVal] = nextEdge;
                        pq.add(new Node(nextEdge, nextVal));
                    }
                }
            }
        }

    }

    static class Node implements Comparable{
        private int edge, value;

        public Node(int edge, int value){
            this.edge = edge;
            this.value = value;
        }

        public int getEdge() {
            return edge;
        }

        public int getValue() {
            return value;
        }

        @Override
        public int compareTo(Object o) {
            Node tmp = (Node)o;
            if(this.getEdge() > ((Node) o).getEdge()){
                return 1;
            }else{
                return -1;
            }
        }
    }
}