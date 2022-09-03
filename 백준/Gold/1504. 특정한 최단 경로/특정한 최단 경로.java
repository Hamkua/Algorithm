import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int n, e;
    static final Integer INF = 200000000; //Integer.MAX_VALUE;
    static ArrayList<Node>[] data;
    static boolean[] visited;
    static int[] result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());



        data = new ArrayList[n + 1];
        for(int i = 0; i<n+1; i++){
            data[i] = new ArrayList();
        }



        for(int i = 0; i < e; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int edge = Integer.parseInt(st.nextToken());

//            data[start].offer(new Node(end, edge));    // offer add 차이?

            data[start].add(new Node(edge, end));
            data[end].add(new Node(edge, start));
        }

        st = new StringTokenizer(br.readLine());
        int v1 = Integer.parseInt(st.nextToken());
        int v2 = Integer.parseInt(st.nextToken());


        int[] vertexV0 = dijkstra(1);
        int[] vertexV1 = dijkstra(v1);
        int[] vertexV2 = dijkstra(v2);

        int result = Math.min(vertexV0[v1] + vertexV1[v2] + vertexV2[n], vertexV0[v2] + vertexV2[v1] + vertexV1[n]);
        result = (result < INF)? result : -1;
        System.out.println(result);

    }

    public static int[] dijkstra(int start){
        PriorityQueue<Node> pq = new PriorityQueue();
        pq.offer(new Node(0, start));

        result = new int[n + 1];
        visited = new boolean[n + 1];

        Arrays.fill(result, INF);
        result[start] = 0;

        Arrays.fill(visited, false);





        while(!pq.isEmpty()){
            Node node = pq.poll();
            int currentEdge = node.edge;
            int currentNode = node.destination;

            if(!visited[currentNode]) {
                visited[currentNode] = true;

                for (Node nextNode : data[currentNode]) {
                    int edge = nextNode.edge;
                    int destination = nextNode.destination;
//                System.out.println(edge + ", " + destination);

                    if (edge < INF) {
                        int nextEdge = currentEdge + edge;
                        if (!visited[destination] && result[destination] > nextEdge) {
                            result[destination] = nextEdge;
                            pq.offer(new Node(nextEdge, destination));
                        }
                    }
                }

            }
        }
        return result;
    }

    static class Node implements Comparable<Node>{
        int edge;
        int destination;

        public Node( int edge, int destination){
            this.edge = edge;
            this.destination = destination;

        }

        @Override
        public int compareTo(Node o) {
            return edge - o.edge;
        }
    }
}


