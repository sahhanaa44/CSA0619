#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>

#define SIZE 100000
#define THREADS 5

int arr[SIZE];

typedef struct
{
    int key;
} SearchData;

int binarySearch(int key)
{
    int low = 0;
    int high = SIZE - 1;

    while(low <= high)
    {
        int mid = (low + high) / 2;

        if(arr[mid] == key)
            return mid;
        else if(arr[mid] < key)
            low = mid + 1;
        else
            high = mid - 1;
    }

    return -1;
}

void *searchThread(void *arg)
{
    SearchData *data = (SearchData *)arg;

    int result = binarySearch(data->key);

    if(result != -1)
        printf("Key %d found at index %d\n", data->key, result);
    else
        printf("Key %d not found\n", data->key);

    pthread_exit(NULL);
}

int main()
{
    int i;

    for(i = 0; i < SIZE; i++)
        arr[i] = i + 1;

    pthread_t threads[THREADS];

    SearchData data[THREADS] =
    {
        {250},
        {5000},
        {25000},
        {75000},
        {99999}
    };

    clock_t start = clock();

    for(i = 0; i < THREADS; i++)
        pthread_create(&threads[i], NULL, searchThread, &data[i]);

    for(i = 0; i < THREADS; i++)
        pthread_join(threads[i], NULL);

    clock_t end = clock();

    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("\nExecution Time = %.6f seconds\n", time_taken);

    return 0;
}
