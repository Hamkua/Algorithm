package baekjoon;
import java.util.*;


public class Main {
    static int[][] graph;
    static int[] visited;
    public static void bfs(int start){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = 1;
        int q;
        int result = 0;
        while(!queue.isEmpty()){
            q = queue.remove();

            for(int i = 1; i<graph.length; i++){
                if(graph[q][i] != 0 && visited[i]!=1){
                    queue.add(i);
                    visited[i] = 1;
                    result += 1;
                }
            }

        }
        System.out.println(result);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        graph = new int[n+1][n+1];
        visited = new int[n+1];
        int a, b;
        for(int i = 0; i<m; i++){
            a = sc.nextInt();
            b = sc.nextInt();

            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        bfs(1);

    }
}
