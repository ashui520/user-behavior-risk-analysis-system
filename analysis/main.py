from data_loader import DataLoader
from feature_engineering import FeatureEngineer
from report_generator import ReportGenerator
from risk_detector import RiskDetector


def main() -> None:
    loader = DataLoader("../data/logs.csv")
    raw_df = loader.load_logs()
    clean_df = loader.clean_logs(raw_df)

    engineer = FeatureEngineer()
    feature_df = engineer.build_user_features(clean_df)

    detector = RiskDetector()
    risk_df = detector.score_risk(feature_df)

    reporter = ReportGenerator()
    reporter.generate_summary(feature_df)
    reporter.generate_risk_report(risk_df)


if __name__ == "__main__":
    main()