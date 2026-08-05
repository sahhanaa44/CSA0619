#include <stdio.h>

typedef struct
{
    int patientID;
    int priority;
    int scanTime;
} ScanRecord;

void merge(ScanRecord arr[], int left, int mid, int right)
{
    int i, j, k;

    int n1 = mid - left + 1;
    int n2 = right - mid;

    ScanRecord L[n1], R[n2];

    for(i = 0; i < n1; i++)
        L[i] = arr[left + i];

    for(j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    i = 0;
    j = 0;
    k = left;

    while(i < n1 && j < n2)
    {
        if(L[i].priority >= R[j].priority)
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while(i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }

    while(j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(ScanRecord arr[], int left, int right)
{
    if(left < right)
    {
        int mid = left + (right - left) / 2;

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

void display(ScanRecord arr[], int n)
{
    int i;

    printf("\nPatientID\tPriority\tScanTime\n");

    for(i = 0; i < n; i++)
    {
        printf("%d\t\t%d\t\t%d\n",
               arr[i].patientID,
               arr[i].priority,
               arr[i].scanTime);
    }
}

int main()
{
    ScanRecord records[] =
    {
        {101,2,35},
        {102,5,20},
        {103,3,15},
        {104,5,18},
        {105,1,45},
        {106,4,22}
    };

    int n = sizeof(records)/sizeof(records[0]);

    printf("Original Patient Scan Records\n");
    display(records,n);

    mergeSort(records,0,n-1);

    printf("\nSorted Patient Scan Records (Highest Priority First)\n");
    display(records,n);

    return 0;
}
