int solution(int number) {
    int output = 0;
	for (int i = 0; i < number; i++){
        if (i % 3 == 0 || i % 5 == 0){
              output += i;
        }
    }
    return output;
}