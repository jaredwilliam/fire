# Defines the data models and calculation logic
class RetirementCalculator:

    def __init__(
        self,
        current_age: int,
        retirement_age: int,
        current_savings: float,
        annual_expenses: float,
        annual_contribution: float,
        rate_of_return: float,
        withdrawal_rate: float,
        inflation_rate: float,
    ):
        self.current_age = current_age
        self.retirement_age = retirement_age
        self.current_savings = current_savings
        self.annual_expenses = annual_expenses
        self.annual_contribution = annual_contribution
        self.rate_of_return = rate_of_return
        self.withdrawal_rate = withdrawal_rate
        self.inflation_rate = inflation_rate

    def calc_years_to_retirement(self) -> int:
        return self.retirement_age - self.current_age

    def calc_future_savings(self) -> float:
        years = self.calc_years_to_retirement()
        future_savings = self.current_savings
        for _ in range(years):
            future_savings = (
                future_savings * (1 + self.rate_of_return) + self.annual_contribution
            )
        return future_savings

    def adjust_expenses_for_inflation(self) -> float:
        years = self.calc_years_to_retirement()
        adjusted_expenses = self.annual_expenses * ((1 + self.inflation_rate) ** years)
        return adjusted_expenses

    def calc_required_savings(self) -> float:
        adjusted_expenses = self.adjust_expenses_for_inflation()
        required_savings = adjusted_expenses / self.withdrawal_rate
        return required_savings

    def run_simulation(self) -> None:
        future_savings = self.calc_future_savings()
        required_savings = self.calc_required_savings()
        years_to_retirement = self.calc_years_to_retirement()
        annual_expenses = self.adjust_expenses_for_inflation()

        is_financially_secure = future_savings >= required_savings

        return {
            "years_to_retirement": years_to_retirement,
            "future_savings": future_savings,
            "required_savings": required_savings,
            "adjusted_expenses": annual_expenses,
            "is_financially_secure": is_financially_secure,
        }


if __name__ == "__main__":

    rc = RetirementCalculator(34, 55, 100000, 8000 * 12, 25000, 0.10, 0.04, 0.03)

    print(rc.run_simulation())
