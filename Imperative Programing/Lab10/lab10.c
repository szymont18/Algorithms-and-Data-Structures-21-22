#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define MAX_STR_LEN 64

typedef struct Vector {
    void *data;
    size_t element_size;
    size_t size;
    size_t capacity;
} Vector;

typedef struct Person {
    int age;
    char first_name[MAX_STR_LEN];
    char last_name[MAX_STR_LEN];
} Person;

// Allocate vector to initial capacity (block_size elements),
// Set element_size, size (to 0), capacity
void init_vector(Vector *vector, size_t block_size, size_t element_size){
    vector->data = malloc(block_size * element_size);
    vector->element_size = element_size;
    vector->size = 0; //Nic na razie nie wpisuje
    vector->capacity = block_size;

}

// If new_capacity is greater than the current capacity,
// new storage is allocated, otherwise the function does nothing.
void reserve(Vector *vector, size_t new_capacity){
    if (new_capacity > vector->capacity){
        vector->data = realloc(vector->data, new_capacity * vector->element_size);
        vector->capacity = new_capacity;
    }
    //W przeciwym przypadku zostawiam jak jest
}

// Resizes the vector to contain new_size elements.
// If the current size is greater than new_size, the container is
// reduced to its first new_size elements.

// If the current size is less than new_size,
// additional zero-initialized elements are appended
void resize(Vector *vector, size_t new_size){
    if (vector->size < new_size){

        char *start = (char *)vector->data;

        for(int i = 0; i < vector->size; i++) start = start + vector->element_size;


        for(size_t j = vector->size; j < new_size; j++){
            memcpy(start, calloc(1, vector->element_size), vector->element_size);
            start = start + vector->element_size;
        }
    }
    vector->size = new_size;
}

// Add element to the end of the vector
void push_back(Vector *vector, void *value){
    if (vector->capacity == vector->size){
        reserve(vector, vector->capacity * 2); //Dodatkowa podwójna pamięć
    }

    char *start = (char *) vector->data; // 1 char = 1 bajt

    for(int i = 0; i < vector->size; i++) start = start + vector->element_size;
    memcpy(start, value, vector->element_size);

    vector->size++;

}

// Remove all elements from the vector
void clear(Vector *vector){
    vector->size = 0;
    //free(vector->data); Nie bo w poleceniu tylko usunać elementy( nie pamieć)
}

// Remove the last element from the vector
void pop_back(Vector *vector){
   vector->size--;
}

// Insert new element at index (0 <= index <= size) position
void insert(Vector *vector, int index, void *value){
    if(vector->size + 1 > vector->capacity) reserve(vector, vector->capacity * 2);

    if(index == vector->size) {
        push_back(vector, value);
        return;
    }
    char *new_el = (char *) vector->data;
    for(int i = 0; i < index; i++) new_el = new_el + vector->element_size;

    size_t rest_size = (vector->size - index)*vector->element_size;

    memmove(new_el + vector->element_size, new_el, rest_size);
    memcpy(new_el,value,vector->element_size);
    vector->size++;
}

// Erase element at position index
void erase(Vector *vector, int index){
    char *start = (char *)vector->data;
    for(int i = 0; i < index; i++) start = start + vector->element_size;
    size_t how_much = (vector->size - index - 1)*vector->element_size;
    memmove(start, start + vector->element_size, how_much);
    vector->size--;
}

// Erase all elements that compare equal to value from the container
void erase_value(Vector *vector, void *value, int(*cmp)(const void*, const void*)){
    char *start = (char *)vector->data;

    int actual_size = vector->size;
    int i = 0;
    while (i < actual_size){
        if(cmp(start,value) == 0){
            erase(vector, i);
            actual_size--;
        }
        else{
            i++;
            start += vector->element_size;
        }
    }


}

// Erase all elements that satisfy the predicate from the vector
void erase_if(Vector *vector, int (*predicate)(void *)){
    char *start = (char *)vector->data;

    int actual_size = vector->size;
    int i = 0;
    while (i < actual_size){
        if(predicate(start) == 1){
            erase(vector, i);
            actual_size--;
        }
        else{
            i++;
            start += vector->element_size;
        }
    }


}

// Request the removal of unused capacity
void shrink_to_fit(Vector *vector){
    size_t new_size = vector->size * vector->element_size;

    vector->data = realloc(vector->data, new_size);
    vector->capacity = vector->size;
}

// Print integer vector
void print_vector_int(Vector *vector){
    printf("%zu\n", vector->capacity);
    int *start = (int*) vector->data;

    for(int i = 0; i < vector->size; i++){
        int el2print = start[i];
        printf("%d ", el2print);
    }
}

// Print char vector
void print_vector_char(Vector *vector){
    printf("%zu\n", vector->capacity);
    char *start = (char*) vector->data;

    for(int i = 0; i < vector->size; i++){
        char el2print = start[i];
        printf("%c ", el2print);
    }
}

// Print vector of Person
void print_vector_person(Vector *vector){
    printf("%zu\n", vector->capacity);
    Person *start = (Person *) vector->data;

    for(int i = 0; i < vector->size; i++){
        Person el2print = start[i];
        printf("%d %s %s\n", el2print.age, el2print.first_name, el2print.last_name);
    }
}

// integer comparator - increasing order
int int_cmp(const void *v1, const void *v2){
    int num1 = *(int*)v1;
    int num2 = *(int*)v2;
    if (num1 < num2) return -1;
    if (num1 > num2) return 1;
    return 0;// num1 == num2
}

// char comparator - lexicographical order (case sensitive)
int char_cmp(const void *v1, const void *v2){
    char c1 = *(char*)v1;
    char c2 = *(char*)v2;

    if (c1 < c2) return -1;
    if (c1 > c2) return 1;

    return 0;
}

// Person comparator:
// Sort according to age (decreasing)
// When ages equal compare first name and then last name
int person_cmp(const void *p1, const void *p2){
    Person per1 = *(Person*)p1;
    Person per2 = *(Person*)p2;

    if(per1.age > per2.age) return -1;
    else if(per1.age < per2.age) return 1;
    else{
        int flag = strcmp(per1.first_name, per2.first_name);
        if (flag != 0) return flag;
        else{
            return strcmp(per1.last_name, per2.last_name);
        }
    }
    return 0; //Wszystko jest takie same
}

// predicate: check if number is even
int is_even(void *value){
    int val = *(int *) value;
    if ((val % 2) == 0) return 1;
    return 0;
}

// predicate: check if char is a vowel
int is_vowel(void *value){
    char *text = (char *) value;
    if(strchr("aeiouyAEIOUY", *text)) return 1;
    return 0;
}

// predicate: check if person is older than 25
int is_older_than_25(void *person){
    Person p1 = *(Person*)person;
    if(p1.age > 25) return 1;
    return 0;
}

// -------------------------------------------------------------

void read_int(void* value) {
    scanf("%d", (int*)value);
}

void read_char(void* value) {
    char c[2];
    scanf("%s", c);
    *(char*)value = c[0];
}

void read_person(void* value) {
    Person *person = (Person*)value;
    scanf("%d %s %s", &person->age, person->first_name, person->last_name);
}

void vector_test(Vector *vector, int n, void(*read)(void*),
                 int (*cmp)(const void*, const void*), int(*predicate)(void*)) {
    char op[2];
    int index;
    size_t size;
    void *v = malloc(vector->element_size);
    for (int i = 0; i < n; ++i) {
        scanf("%s", op);
        switch (op[0]) {
            case 'p': // push_back
                read(v);
                push_back(vector, v);
                break;
            case 'i': // insert
                scanf("%d", &index);
                read(v);
                insert(vector, index, v);
                break;
            case 'e': // erase
                scanf("%d", &index);
                read(v);
                erase(vector, index);
                erase_value(vector, v, cmp);
                break;
            case 'd': // erase (predicate)
                erase_if(vector, predicate);
                break;
            case 'r': // resize
                scanf("%zu", &size);
                resize(vector, size);
                break;
            case 'c': // clear
                clear(vector);
                break;
            case 'f': // shrink
                shrink_to_fit(vector);
                break;
            case 's': // sort
                qsort(vector->data, vector->size,
                      vector->element_size, cmp);
                break;
            default:
                printf("No such operation: %s\n", op);
                break;
        }
    }
    free(v);
}

int main(void) {
    int to_do, n;
    Vector vector_int, vector_char, vector_person;

    scanf("%d%d", &to_do, &n);

    switch (to_do) {
        case 1:
            init_vector(&vector_int, 4, sizeof(int));
            vector_test(&vector_int, n, read_int, int_cmp, is_even);
            print_vector_int(&vector_int);
            free(vector_int.data);
            break;
        case 2:
            init_vector(&vector_char, 2, sizeof(char));
            vector_test(&vector_char, n, read_char, char_cmp, is_vowel);
            print_vector_char(&vector_char);
            free(vector_char.data);
            break;
        case 3:
            init_vector(&vector_person, 2, sizeof(Person));
            vector_test(&vector_person, n, read_person, person_cmp, is_older_than_25);
            print_vector_person(&vector_person);
            free(vector_person.data);
            break;
        default:
            printf("Nothing to do for %d\n", to_do);
            break;
    }

    return 0;
}

