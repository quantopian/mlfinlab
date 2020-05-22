"""
Initialize Online Portfolio Selection Module.
"""
# Parent Class
from mlfinlab.online_portfolio_selection.online_portfolio_selection import OLPS
from mlfinlab.online_portfolio_selection.universal_portfolio import UP

# Benchmarks
from mlfinlab.online_portfolio_selection.benchmarks.buy_and_hold import BAH
from mlfinlab.online_portfolio_selection.benchmarks.best_stock import BestStock
from mlfinlab.online_portfolio_selection.benchmarks.constant_rebalanced_portfolio import CRP
from mlfinlab.online_portfolio_selection.benchmarks.best_constant_rebalanced_portfolio import BCRP

# Momentum
from mlfinlab.online_portfolio_selection.momentum.exponential_gradient import EG
from mlfinlab.online_portfolio_selection.momentum.follow_the_leader import FTL
from mlfinlab.online_portfolio_selection.momentum.follow_the_regularized_leader import FTRL

# Mean Reversion
from mlfinlab.online_portfolio_selection.mean_reversion.robust_median_reversion import RMR
from mlfinlab.online_portfolio_selection.mean_reversion.passive_aggressive_mean_reversion import PAMR
from mlfinlab.online_portfolio_selection.mean_reversion.confidence_weighted_mean_reversion import CWMR
from mlfinlab.online_portfolio_selection.mean_reversion.online_moving_average_reversion import OLMAR

# Pattern Matching
from mlfinlab.online_portfolio_selection.pattern_matching.correlation_driven_nonparametric_learning import CORN
from mlfinlab.online_portfolio_selection.pattern_matching.correlation_driven_nonparametric_learning_uniform import CORNU
from mlfinlab.online_portfolio_selection.pattern_matching.correlation_driven_nonparametric_learning_k import CORNK
from mlfinlab.online_portfolio_selection.pattern_matching.symmetric_correlation_driven_nonparametric_learning import SCORN
from mlfinlab.online_portfolio_selection.pattern_matching.symmetric_correlation_driven_nonparametric_learning_k import SCORNK
from mlfinlab.online_portfolio_selection.pattern_matching.functional_correlation_driven_nonparametric_learning import FCORN
from mlfinlab.online_portfolio_selection.pattern_matching.functional_correlation_driven_nonparametric_learning_k import FCORNK
