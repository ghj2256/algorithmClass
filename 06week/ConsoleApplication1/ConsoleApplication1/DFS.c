#include <stdio.h>
#include <stdbool.h>
#define N 9

bool visited[9];
int graph[9][3] = { {NULL}, {2,3,8}, {1,7}, {1,4,5}, {3,5}, {3,4}, {7}, {2,6,8}, {1,7} };

void dfs(int x) {
    visited[x] = true;
    printf("%d ", x);
    for (int i = 0; i <= N; i++) {
        if (graph[x][i] && !visited[i])
            dfs(i);
    }
}

int main() {
    dfs(1);
}