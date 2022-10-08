//2022-10-08
public static void main(String[] args) {
        String json = ""}";
        for (int i = 0; i < 10; i++) { 
            long l = System.currentTimeMillis();
            System.out.println(signWithS(JSONUtil.toBean(json, Map.class), "xxxx"));
          
        }
