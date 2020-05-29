package main;

import java.util.HashMap;
import java.util.Map;

/*
 * https://codingbat.com/prob/p148813
 * Modify and return the given map as follows: if the key "a" has a value, set the key "b" to have that same value. In all cases remove the key "c", leaving the rest of the map unchanged.
 * 
 * mapShare({"a": "aaa", "b": "bbb", "c": "ccc"}) → {"a": "aaa", "b": "aaa"}
 * mapShare({"b": "xyz", "c": "ccc"}) → {"b": "xyz"}
 * mapShare({"a": "aaa", "c": "meh", "d": "hi"}) → {"a": "aaa", "b": "aaa", "d": "hi"}
 */
public class MapShare {
	public Map<String, String> mapShare(Map<String, String> map) {
		Map<String, String> result = new HashMap<String, String>();
		if (map.containsKey("a")) {
			map.put("b", map.get("a"));
		}
		if (map.containsKey("c")) {
			map.remove("c");
		}
		result.putAll(map);
		return result;
	}
}
