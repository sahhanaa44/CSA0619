#include <stdio.h>
#include <string.h>

int main() {
    int n,i,pos=-1;
    char products[50][30],key[30];

    printf("Enter number of products: ");
    scanf("%d",&n);

    printf("Enter product names:\n");
    for(i=0;i<n;i++)
        scanf("%s",products[i]);

    printf("Enter product to search: ");
    scanf("%s",key);

    for(i=0;i<n;i++){
        if(strcmp(products[i],key)==0){
            pos=i;
            break;
        }
    }

    if(pos!=-1)
        printf("Product found at position %d\n",pos+1);
    else
        printf("Product not found\n");

    return 0;
}
