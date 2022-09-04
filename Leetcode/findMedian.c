// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>




typedef struct Node {
    int n;
    struct Node *next;
} MedianFinder;


MedianFinder* medianFinderCreate() {
    MedianFinder *head = malloc(sizeof(MedianFinder));
    head->next = NULL;
    head->n = -100000;
    if (head == NULL)
        return (NULL);
    return head;
}

MedianFinder *medianFinderAddNum(MedianFinder* obj, int num) {
    MedianFinder *new = NULL;
    MedianFinder *ptr = NULL;
    MedianFinder *prev = NULL;
    
    if (obj->n == -100000)
    {
        obj->n = num;
        return (obj);
    }
    new = malloc(sizeof(MedianFinder));
    if (new == NULL)
        return (NULL);
    ptr = obj;
    while (ptr != NULL)
    {
        if (ptr->n >= num)
            break;
        prev = ptr;
        ptr = ptr->next;
    }
    new->n = num;
    
    new->next = ptr;
    if (prev != NULL)
        prev->next = new;
    else
        obj = new;

    return (obj);
        
}

double medianFinderFindMedian(MedianFinder* obj) {
    
    MedianFinder *ptr = NULL;
    
    ssize_t index = 0, mid = 0;
    int is_med = 0;
    
    ptr = obj;
    while (ptr != NULL)
    {
        index++;
        ptr = ptr->next;
    }
    if (index == 1)
        return (obj->n);
    mid = index / 2;
    ptr = obj;
    if (index % 2 != 0)
        is_med = 1;
    index = 0;
    while (index < (mid - 1))
    {
        ptr = ptr->next;
        index++;
    }
    if (is_med)
        return ((ptr->next)->n);
    return ( (float)((ptr->n + (ptr->next)->n)) / 2 );
}

void medianFinderFree(MedianFinder* obj) {
    MedianFinder *ptr = obj;
    while (ptr != NULL)
    {
        obj = ptr->next;
        free(ptr);
        ptr = obj;
    }
}


int main() {
    int arr[5] = {-1, -2, -3, -4, -5};
    // int arr[5] = {1,2,3,4,5,6};
    MedianFinder* obj = medianFinderCreate();
    for (int i = 0; i < 5; i++)
    {
        int num = arr[i];
        obj = medianFinderAddNum(obj, num); 
        double param_2 = medianFinderFindMedian(obj);
        printf("%f \n", param_2);
    }
    medianFinderFree(obj);
    return 0;
}
