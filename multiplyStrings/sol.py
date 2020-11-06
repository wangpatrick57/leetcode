class Solution {
    public String multiply(String num1, String num2) {
        int[] digits = new int[num1.length() + num2.length()];

        for (int i = 0; i < num1.length(); i++) {
            for (int j = 0; j < num2.length(); j++) {
                int digits_pos = digits.length - 1 - i - j;
                int tens_pos = digits.length - 1 - i - j - 1;
                int digit1 = num1.charAt(num1.length() - 1 - i) - 48;
                int digit2 = num2.charAt(num2.length() - 1 - j) - 48;
                int product = digit1 * digit2;

                // System.out.println("i = " + i + " j = " + j + " digits_pos = " + digits_pos + " digit1 = " + digit1 + " digit2 = " + digit2);

                digits[digits_pos] += product % 10;
                digits[tens_pos] += product / 10;

                if (digits[digits_pos] >= 10) {
                    digits[tens_pos] += digits[digits_pos] / 10;
                    digits[digits_pos] %= 10;
                }
            }
        }

        StringBuilder builder = new StringBuilder();
        boolean leadingEnded = false;

        for (int i = 0; i < digits.length; i++) {
            if (digits[i] != 0) {
                leadingEnded = true;
            }

            if (leadingEnded || i == digits.length - 1) {
                builder.append(digits[i]);
            }
        }

        return builder.toString();
    }
}
