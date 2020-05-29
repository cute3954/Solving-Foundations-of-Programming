package main;

import java.util.HashMap;
import java.util.Map;

public class MapShare_main {

	public static void main(String[] args) {
		Map<String, String> map = new HashMap<String, String>();
		map.put("a", "aaa");
		map.put("b", "bbb");
		map.put("c", "ccc");
		MapShare mapShare = new MapShare();
		Map<String, String> result = mapShare.mapShare(map);
		System.out.println(result);
	}

}
