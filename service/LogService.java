import java.util.ArrayList;
import java.util.List;

public class LogService {
    private final List<UserBehavior> logs = new ArrayList<>();

    public void addLog(UserBehavior behavior) {
        logs.add(behavior);
        System.out.println("新增日志：" + behavior);
    }

    public List<UserBehavior> getLogsByUser(String userId) {
        List<UserBehavior> result = new ArrayList<>();
        for (UserBehavior log : logs) {
            if (log.getUserId().equals(userId)) {
                result.add(log);
            }
        }
        return result;
    }

    public int countUserActions(String userId) {
        int count = 0;
        for (UserBehavior log : logs) {
            if (log.getUserId().equals(userId)) {
                count++;
            }
        }
        return count;
    }
}