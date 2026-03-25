public class UserBehavior {
    private final String userId;
    private final String action;
    private final String page;
    private final String ip;
    private final String timestamp;

    public UserBehavior(String userId, String action, String page, String ip, String timestamp) {
        this.userId = userId;
        this.action = action;
        this.page = page;
        this.ip = ip;
        this.timestamp = timestamp;
    }

    public String getUserId() {
        return userId;
    }

    public String getAction() {
        return action;
    }

    public String getPage() {
        return page;
    }

    public String getIp() {
        return ip;
    }

    public String getTimestamp() {
        return timestamp;
    }

    @Override
    public String toString() {
        return "UserBehavior{"
                + "userId='" + userId + '\''
                + ", action='" + action + '\''
                + ", page='" + page + '\''
                + ", ip='" + ip + '\''
                + ", timestamp='" + timestamp + '\''
                + '}';
    }
}