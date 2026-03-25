public class RiskRuleEngine {

    public int calculateRiskScore(
            int totalActions,
            double avgActionPerSecond,
            int uniquePages,
            int clickCount
    ) {
        int score = 0;

        if (totalActions >= 8) {
            score += 40;
        }
        if (avgActionPerSecond >= 0.8) {
            score += 35;
        }
        if (uniquePages <= 1 && clickCount >= 5) {
            score += 25;
        }

        return score;
    }

    public String getRiskLevel(int score) {
        if (score >= 70) {
            return "高风险";
        } else if (score >= 40) {
            return "中风险";
        } else {
            return "低风险";
        }
    }
}