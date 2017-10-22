import UIKit
import UserNotifications
import FirebaseDatabase

class ViewController: UIViewController {

    var timer = Timer()
    var ref: DatabaseReference!
    var firstTime = true
    var secondTime = false

    func scheduledTimerWithTimeInterval(){
        // Scheduling timer to Call the function "updateCounting" with the interval of 1 seconds
        timer = Timer.scheduledTimer(timeInterval: 3, target: self, selector: #selector(self.pollFirebase), userInfo: nil, repeats: true)
    }

    override func viewDidLoad() {
        ref = Database.database().reference()
        scheduledTimerWithTimeInterval()
    }

    func pollFirebase(){
        ref.observe(DataEventType.value, with: { (snapshot) in
            let postDict = snapshot.value as? [String : AnyObject] ?? [:]
            if let hasLowStock = postDict["hasLowStocks"] as? Int {
                if hasLowStock == 1 && self.firstTime {
                    let alertController = UIAlertController(
                        title: "Low stock alert",
                        message: "Would you like to re-order all stocks that are low in quantity?",
                        preferredStyle: .alert)

                    let defaultAction = UIAlertAction(title: "OK",
                                                      style: .default,
                                                      handler: { (alert) in
                                                        self.secondTime = true
                    })
                    let cancelAction = UIAlertAction(title: "Cancel", style: .default, handler: nil)
                    alertController.addAction(defaultAction)
                    alertController.addAction(cancelAction)

                    self.present(alertController, animated: true, completion: nil)
                    self.firstTime = false
                } else if hasLowStock == 1 && self.secondTime {
                    let alertController = UIAlertController(
                        title: "Stocks have been re-ordered.", message: nil,
                        preferredStyle: .alert)

                    let defaultAction = UIAlertAction(title: "OK", style: .default, handler: nil)
                    alertController.addAction(defaultAction)

                    self.present(alertController, animated: true, completion: nil)
                    self.secondTime = false
                }
            }
        })
    }
    override var prefersStatusBarHidden: Bool {
        return true
    }

}
